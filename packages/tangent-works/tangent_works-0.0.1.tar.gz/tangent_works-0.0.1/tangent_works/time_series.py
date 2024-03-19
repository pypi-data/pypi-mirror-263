import io
import json
from typing import Any, Dict, Optional
import pandas as pd
import requests

from .authentication import TIMLicense
from .api_utils import raise_on_error_response
from .config import get_tim_url


class TimeSeries:
    def __init__(self, license: TIMLicense, dataframe: pd.DataFrame, timestamp: str, timestamp_format: str):
        self._license = license
        self._dataframe = dataframe
        self._timestamp = timestamp
        self._timestamp_format = timestamp_format
        self._group_keys = []
        self._alignment = None
        self._shape = None
        self._sampling_period = self._get_sampling_period()

    @property
    def dataframe(self) -> Optional[pd.DataFrame]:
        return self._dataframe

    @property
    def timestamp(self) -> Optional[str]:
        return self._timestamp

    @property
    def timestamp_format(self) -> Optional[str]:
        return self._timestamp_format

    @property
    def alignment(self) -> Optional[Any]:
        return self._alignment

    @property
    def sampling_period(self) -> Optional[Any]:
        return self._sampling_period

    @property
    def shape(self) -> Optional[Any]:
        return self._shape

    def _get_valid_configuration(self, conf: Optional[dict]):
        if conf is None:
            valid_conf = {}
        else:
            valid_conf = conf.copy()
        if 'timestamp_column' not in valid_conf:
            valid_conf['timestamp_column'] = self._timestamp
        return valid_conf

    @staticmethod
    def _find_minimum_period(x: pd.Series) -> pd.Timedelta:
        return pd.to_datetime(x).diff()[1:].unique().min()  # FIXME time_series timestamp column type

    def _get_minimum_timestamp_difference(self) -> pd.Timedelta | None:
        if self._group_keys:
            grouped = self.dataframe.groupby(self._group_keys)

            min_periods = [self._find_minimum_period(group[self.timestamp]) for _, group in grouped]
            min_periods_filtered = [period for period in min_periods if period is not pd.NaT]
            min_period = min(min_periods_filtered) if min_periods_filtered else pd.NaT
        else:
            min_period = self._find_minimum_period(self.dataframe[self.timestamp])

        return min_period if min_period is not pd.NaT else None

    def _get_sampling_period(self) -> pd.offsets.DateOffset | None:
        sp = self._get_minimum_timestamp_difference()

        if sp is None:
            return None
        elif sp >= pd.Timedelta("365D"):
            n = sp // pd.Timedelta("365D")
            return pd.offsets.DateOffset(months=n * 12)
        elif sp >= pd.Timedelta("28D"):
            n = sp // pd.Timedelta("28D")
            return pd.offsets.DateOffset(months=n)
        elif sp >= pd.Timedelta("0s"):
            n = sp // pd.Timedelta("1s")
            return pd.offsets.DateOffset(seconds=n)
        else:
            return ValueError("Sampling period calculation failed.")

    def time_scale(self, timescale_conf: Optional[Dict[str, Any]]) -> 'TimeSeries':
        endpoint_url = f'{get_tim_url()}/time-scale'
        df_str = self._dataframe.to_csv(index=False) if self._dataframe is not None else ''
        valid_conf = self._get_valid_configuration(timescale_conf)
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

        df = pd.read_csv(io.StringIO(response.text), sep=None)
        new_timeseries_object = TimeSeries(self._license, df, self._timestamp, self._timestamp_format)
        return new_timeseries_object

    def impute(self, impute_conf: Optional[Dict[str, Any]]) -> 'TimeSeries':
        endpoint_url = f'{get_tim_url()}/impute'
        df_str = self._dataframe.to_csv(index=False) if self._dataframe is not None else ''
        valid_conf = self._get_valid_configuration(impute_conf)
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

        df = pd.read_csv(io.StringIO(response.text), sep=None)
        new_timeseries_object = TimeSeries(self._license, df, self._timestamp, self._timestamp_format)
        return new_timeseries_object

    def analyze(self) -> 'TimeSeries':
        return self

    def update(self, ts: 'TimeSeries') -> 'TimeSeries':
        return self
