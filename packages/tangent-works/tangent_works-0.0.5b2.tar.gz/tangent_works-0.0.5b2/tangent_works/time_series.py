import io
import json
from typing import Any, Dict, Optional
import pandas as pd
import requests

from .authentication import TIMLicense
from .api_utils import (
    raise_on_error_response,
    csv_request_part,
    json_request_part,
    response_to_dataframe,
    create_authorization_header
)
from .config import get_tim_url
from .exceptions import ClientValidationError


class TimeSeries:
    def __init__(self, license: TIMLicense, dataframe: pd.DataFrame):
        if not isinstance(license, TIMLicense):
            raise ClientValidationError('Invalid license object type.')

        if not isinstance(dataframe, pd.DataFrame):
            raise ClientValidationError('Invalid dataframe type')

        self._license = license
        self._dataframe = dataframe
        self._group_keys = []

        self._timestamp = self._find_timestamp_column()
        self._sampling_period = self._get_sampling_period()

    @property
    def dataframe(self) -> Optional[pd.DataFrame]:
        return self._dataframe

    @property
    def timestamp(self) -> Optional[str]:
        return self._timestamp

    @property
    def sampling_period(self) -> Optional[Any]:
        return self._sampling_period

    @property
    def shape(self) -> tuple[int, int]:
        return self.dataframe.shape

    def time_scale(self, configuration: Dict[str, Any]) -> 'TimeSeries':
        self._validate_time_scale_call(configuration)

        complete_config = self._create_complete_configuration(configuration)

        response = self._send_time_scale_request(complete_config)

        dataframe = response_to_dataframe(response, timestamp_columns=[self.timestamp])
        new_timeseries_object = TimeSeries(self._license, dataframe)

        return new_timeseries_object

    def _validate_time_scale_call(self, configuration: Dict[str, Any]) -> None:
        if not isinstance(configuration, Dict):
            raise ClientValidationError('Invalid configuration object type.')

    def _send_time_scale_request(self, config: Dict[str, Any]) -> requests.Response:
        endpoint_url = self._get_time_scale_url()
        headers = create_authorization_header(self._license.token)
        parts = self._create_parts_for_multipart_request(config)

        response = requests.post(endpoint_url, headers=headers, files=parts)
        raise_on_error_response(response)

        return response

    def impute(self, configuration: Dict[str, Any]) -> 'TimeSeries':
        self._validate_imputation_call(configuration)

        complete_config = self._create_complete_configuration(configuration)

        response = self._send_imputation_request(complete_config)

        dataframe = response_to_dataframe(response, timestamp_columns=[self.timestamp])
        new_timeseries_object = TimeSeries(self._license, dataframe)

        return new_timeseries_object

    def _validate_imputation_call(self, configuration: Dict[str, Any]) -> None:
        if not isinstance(configuration, Dict):
            raise ClientValidationError('Invalid configuration object type.')

    def _create_complete_configuration(self, config: Dict[str, Any]) -> Dict[str, Any]:
        complete_config = config.copy()
        complete_config['timestamp_column'] = self.timestamp
        return complete_config

    def _send_imputation_request(self, config: Dict[str, Any]) -> requests.Response:
        endpoint_url = self._get_imputation_url()
        headers = create_authorization_header(self._license.token)
        parts = self._create_parts_for_multipart_request(config)

        response = requests.post(endpoint_url, headers=headers, files=parts)
        raise_on_error_response(response)

        return response

    def _find_timestamp_column(self) -> str:
        timestamp_columns_found = []

        for column in self.dataframe.columns:
            if pd.api.types.is_datetime64_any_dtype(self.dataframe[column]):
                timestamp_columns_found.append(column)

        if len(timestamp_columns_found) == 0:
            raise ClientValidationError('Timestamp column not found in the dataframe.')

        if len(timestamp_columns_found) > 1:
            raise ClientValidationError('Multiple timestamp columns found in the dataframe.')

        return timestamp_columns_found[0]

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

    def _get_minimum_timestamp_difference(self) -> pd.Timedelta | None:
        if self._group_keys:
            grouped = self.dataframe.groupby(self._group_keys)

            min_periods = [self._find_minimum_period(group[self.timestamp]) for _, group in grouped]
            min_periods_filtered = [period for period in min_periods if period is not pd.NaT]
            min_period = min(min_periods_filtered) if min_periods_filtered else pd.NaT
        else:
            min_period = self._find_minimum_period(self.dataframe[self.timestamp])

        return min_period if min_period is not pd.NaT else None

    def _find_minimum_period(self, timestamp_column: pd.Series) -> pd.Timedelta:
        return timestamp_column.diff()[1:].unique().min()

    def _get_time_scale_url(self):
        return f'{get_tim_url()}/time-scale'

    def _get_imputation_url(self):
        return f'{get_tim_url()}/impute'

    def _create_parts_for_multipart_request(self, config: Dict[str, Any]) -> list:
        return [
            csv_request_part('dataset', self.dataframe.to_csv(index=False)),
            json_request_part('configuration', json.dumps(config))
        ]
