import json
from typing import Any, Dict, Optional
import pandas as pd
import requests

from .authentication import TIMLicense
from .api_utils import (
    raise_on_error_response,
    create_authorization_header,
    csv_request_part,
    json_request_part,
    response_to_dataframe
)
from .time_series import TimeSeries
from .config import get_tim_url
from .exceptions import ClientValidationError


class Forecasting:

    def __init__(self, license: TIMLicense, time_series: Optional[TimeSeries] = None,
                 configuration: Optional[Dict[str, Any]] = None):

        if not isinstance(license, TIMLicense):
            raise ClientValidationError('Invalid license object type.')

        if not isinstance(time_series, TimeSeries) and time_series is not None:
            raise ClientValidationError('Invalid time-series object type.')

        if not isinstance(configuration, Dict) and configuration is not None:
            raise ClientValidationError('Invalid configuration object type.')

        self._license = license
        self._time_series = time_series
        self._configuration = configuration if configuration else {}
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
    def configuration(self) -> Dict[str, Any]:
        return self._configuration

    @property
    def model(self) -> Optional[Dict[str, Any]]:
        return self._model

    def build_model(self) -> None:
        self._validate_build_model_call()

        complete_config = self._create_complete_configuration(self.configuration, self.time_series)

        response = self._send_build_model_request(self.time_series, complete_config)

        self._model = response.json()

    def _validate_build_model_call(self) -> None:
        if self.model is not None:
            raise ClientValidationError('The model has already been built.')

        if self.time_series is None or self.time_series.dataframe is None:
            raise ClientValidationError('The time-series object has not been set.')

    def _send_build_model_request(self, time_series: TimeSeries, config: Dict[str, Any]) -> requests.Response:
        endpoint_url = self._get_forecasting_build_model_url()
        headers = create_authorization_header(self._license.token)
        parts = self._create_parts_for_multipart_request(time_series, config)

        response = requests.post(endpoint_url, headers=headers, files=parts)
        raise_on_error_response(response)

        return response

    def forecast(self, configuration: Dict[str, Any] = {}, time_series: Optional[TimeSeries] = None) -> pd.DataFrame:
        input_time_series = time_series if time_series is not None else self._time_series
        config = configuration if configuration else {}

        self._validate_forecast_call(config, input_time_series)

        complete_config = self._create_complete_configuration(config, input_time_series)

        response = self._send_forecast_request(input_time_series, complete_config, self.model)

        return response_to_dataframe(response, timestamp_columns=['timestamp'])

    def _validate_forecast_call(self, configuration: Dict[str, Any], input_time_series: TimeSeries) -> None:
        if not isinstance(configuration, Dict):
            raise ClientValidationError('Invalid configuration object type.')

        if not isinstance(input_time_series, TimeSeries):
            raise ClientValidationError('Invalid time-series object type.')

        if input_time_series is None or input_time_series.dataframe is None:
            raise ClientValidationError('The time-series object has not been set.')

        if self.model is None:
            raise ClientValidationError('The model has not been built. Please, first build the model.')

    def _send_forecast_request(self, time_series: TimeSeries, config: Dict[str, Any], model: Dict[str, Any]) -> requests.Response:
        endpoint_url = self._get_forecasting_predict_url()
        headers = create_authorization_header(self._license.token)
        parts = self._create_parts_for_multipart_request(time_series, config, model)

        response = requests.post(endpoint_url, headers=headers, files=parts)
        raise_on_error_response(response)

        return response

    def _create_complete_configuration(self, config: Dict[str, Any], time_series: TimeSeries) -> Dict[str, Any]:
        complete_config = config.copy()
        complete_config['timestamp_column'] = time_series.timestamp
        return complete_config

    def _get_forecasting_build_model_url(self):
        return f'{get_tim_url()}/build-model'

    def _get_forecasting_predict_url(self):
        return f'{get_tim_url()}/predict'

    def _create_parts_for_multipart_request(self, time_series: TimeSeries, config: Dict[str, Any], model: Optional[Dict[str, Any]] = None) -> list:
        parts = [
            csv_request_part('dataset', time_series.dataframe.to_csv(index=False)),
            json_request_part('configuration', json.dumps(config))
        ]

        if model:
            parts.append(json_request_part('model', json.dumps(model)))

        return parts
