import io
import json
from typing import Any, Dict, Optional
import pandas as pd
import requests

from .authentication import TIMLicense
from .api_utils import raise_on_error_response
from .time_series import TimeSeries
from .config import get_tim_url
from .exceptions import ClientValidationError


class Forecasting:

    def __init__(self, license: TIMLicense, ts: Optional[TimeSeries] = None, conf: Optional[Dict[str, Any]] = None):
        self._license = license
        self._time_series = ts
        self._configuration = conf
        self._model = None

    @classmethod
    def from_model(cls, license: TIMLicense, model: Dict[str, Any]) -> 'Forecasting':
        obj = cls(license)
        obj._model = model
        return obj

    @property
    def time_series(self) -> Optional[TimeSeries]:
        return self._time_series

    @property
    def configuration(self) -> Optional[Dict[str, Any]]:
        return self._configuration

    @property
    def model(self) -> Optional[Dict[str, Any]]:
        return self._model

    def build_model(self) -> None:
        endpoint_url = f'{get_tim_url()}/build-model'
        self._validate_time_series_object(self._time_series)
        valid_conf = self._get_valid_configuration(self._time_series, self._configuration)
        df_str = self._time_series.dataframe.to_csv(index=False)
        config_str = json.dumps(valid_conf)

        headers = {
            'Authorization': f'Bearer {self._license.token}'
        }
        files = [
            ('dataset', ('dataset.csv', df_str, 'text/csv')),
            ('configuration', ('configuration.json', config_str, 'application/json'))
        ]
        response = requests.post(endpoint_url, headers=headers, files=files)
        raise_on_error_response(response)

        self._model = response.json()

    def forecast(self, forecast_conf: Dict[str, Any], ts: Optional[TimeSeries] = None) -> pd.DataFrame:
        endpoint_url = f'{get_tim_url()}/predict'
        valid_forecast_time_series = self._get_validated_time_series_object(ts)
        valid_forecast_conf = self._get_valid_configuration(valid_forecast_time_series, forecast_conf)
        df_str = valid_forecast_time_series.dataframe.to_csv(index=False)
        config_str = json.dumps(valid_forecast_conf)
        model_str = json.dumps(self._model) if self._model is not None else '{}'

        headers = {
            'Authorization': f'Bearer {self._license.token}'
        }
        files = [
            ('dataset', ('dataset.csv', df_str, 'text/csv')),
            ('configuration', ('configuration.json', config_str, 'application/json')),
            ('model', ('model.json', model_str, 'application/json')),
        ]
        response = requests.post(endpoint_url, headers=headers, files=files)
        raise_on_error_response(response)

        df = pd.read_csv(io.StringIO(response.text), sep=None, parse_dates=['timestamp'])
        return df

    def _get_validated_time_series_object(self, input_time_series: Optional[TimeSeries]):
        valid_forecast_time_series = input_time_series if input_time_series is not None else self._time_series
        self._validate_time_series_object(valid_forecast_time_series)
        return valid_forecast_time_series

    def _validate_time_series_object(self, ts: Optional[TimeSeries]):
        if ts is None or ts.dataframe is None:
            raise ClientValidationError('The time-series object has not been set.')

    def _get_valid_configuration(self, ts: TimeSeries, conf: Optional[dict]):
        if conf is None:
            valid_conf = {}
        else:
            valid_conf = conf.copy()
        if 'timestamp_column' not in valid_conf:
            valid_conf['timestamp_column'] = ts.timestamp
        return valid_conf

    def explain(self) -> None:
        pass

    def visualize(self) -> None:
        pass
