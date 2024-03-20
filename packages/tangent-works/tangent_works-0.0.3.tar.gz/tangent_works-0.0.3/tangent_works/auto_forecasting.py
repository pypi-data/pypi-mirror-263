from typing import Any, Dict, List, Optional
import logging
from dataclasses import dataclass
import pandas as pd
import numpy as np

from .authentication import TIMLicense
from .time_series import TimeSeries
from .forecasting import Forecasting
from .general_utils import is_optional_list_of_elements, is_optional_isinstance
from .exceptions import ClientValidationError


@dataclass
class DataConfiguration:
    in_sample_rows: Optional[List] = None
    out_of_sample_rows: Optional[List] = None
    columns: Optional[List] = None
    imputation: Optional[Dict] = None
    time_scaling: Optional[Dict] = None
    last_target_timestamp: Optional[pd.Timestamp] = None

    def __post_init__(self):
        assert is_optional_list_of_elements(self.in_sample_rows, tuple)
        assert is_optional_list_of_elements(self.out_of_sample_rows, tuple)
        assert is_optional_list_of_elements(self.columns, str)
        assert is_optional_isinstance(self.imputation, dict)
        assert is_optional_isinstance(self.time_scaling, dict)
        assert is_optional_isinstance(self.last_target_timestamp, pd.Timestamp)

    @classmethod
    def from_dict(cls, configuration):
        data_conf_dict = configuration.get('data', {})
        return cls(
            in_sample_rows=cls._convert_rows(data_conf_dict.get('in_sample_rows')),
            out_of_sample_rows=cls._convert_rows(data_conf_dict.get('out_of_sample_rows')),
            columns=data_conf_dict.get('columns'),
            imputation=data_conf_dict.get('imputation'),
            time_scaling=data_conf_dict.get('time_scaling'),
            last_target_timestamp=None)

    @classmethod
    def _convert_rows(cls, rows):
        if rows is None:
            return None
        else:
            return [(pd.to_datetime(row['from']), pd.to_datetime(row['to'])) for row in rows]


class AutoForecasting:

    def __init__(self, license: TIMLicense, time_series: TimeSeries, configuration: Optional[Dict[str, Any]] = None):
        self._license = license
        self._configuration = configuration
        self._time_series = time_series
        self._data_configuration = DataConfiguration.from_dict(configuration) if configuration is not None else DataConfiguration()
        self._model = None
        self._result_table = None
        self._accuracies = None

    @property
    def result_table(self) -> Optional[Any]:
        return self._result_table

    @property
    def accuracies(self) -> Optional[Any]:
        return self._accuracies

    @property
    def model(self) -> Optional[Any]:
        return self._model

    def run(self):
        processed_time_series = self.get_processed_time_series()
        self._set_last_target_timestamp(processed_time_series)
        self._set_rows(processed_time_series)
        self._model = self._run_build(processed_time_series)
        self._result_table = self._run_forecast(processed_time_series)
        self._accuracies = self._calculate_accuracies()

    def get_processed_time_series(self) -> TimeSeries:
        processed_time_series = self._time_series
        processed_time_series = self._select_columns(processed_time_series)
        processed_time_series = self._run_time_scaling(processed_time_series)
        processed_time_series = self._run_imputation(processed_time_series)

        return processed_time_series

    def _select_columns(self, input_time_series: TimeSeries) -> TimeSeries:
        if self._data_configuration.columns is not None:
            columns = [self._time_series.timestamp] + self._data_configuration.columns
            return self._new_time_series(input_time_series.dataframe[columns])
        else:
            return input_time_series

    def _run_time_scaling(self, input_time_series: TimeSeries) -> TimeSeries:
        if self._data_configuration.time_scaling is not None:
            logging.info("Running time-scale.")
            config = {'time_scaling': self._data_configuration.time_scaling}
            return input_time_series.time_scale(config)
        else:
            return input_time_series

    def _run_imputation(self, input_time_series: TimeSeries) -> TimeSeries:
        if self._data_configuration.imputation is not None:
            logging.info("Running imputation.")
            config = {'imputation': self._data_configuration.imputation}
            return input_time_series.impute(config)
        else:
            return input_time_series

    def _run_build(self, input_time_series: TimeSeries) -> Forecasting:
        logging.info("Running build-model.")
        build_time_series = self._get_build_time_series(input_time_series)
        build_configuration = self._get_build_configuration(input_time_series)

        forecasting = Forecasting(self._license, build_time_series, build_configuration)
        forecasting.build_model()

        return forecasting.model

    def _run_forecast(self, input_time_series: TimeSeries) -> pd.DataFrame:
        logging.info("Running forecast.")
        forecasting = Forecasting.from_model(self._license, self._model)
        forecast_time_series = self._get_forecast_series(input_time_series)
        forecast_configuration = self._get_forecast_configuration()
        result_table = forecasting.forecast(forecast_configuration, forecast_time_series)

        return self._select_result_rows(result_table)

    def _calculate_accuracies(self):
        if self._result_table is None:
            return None
        else:
            cleaned_df = self._result_table.dropna(subset=['target', 'forecast'])
            absolute_errors = np.abs(cleaned_df['target'] - cleaned_df['forecast'])
            return absolute_errors.mean()

    def _get_target_column_name(self, input_time_series: TimeSeries):
        if self._engine_configuration_exists() and 'target_column' in self._configuration['engine']:
            target_column = self._configuration['engine']['target_column']
            if target_column not in input_time_series.dataframe.columns:
                raise ClientValidationError(f"Target column '{target_column}' is not present in the dataset. Please choose a valid target column.")
        else:
            target_column = next((column for column in input_time_series.dataframe.columns if column != input_time_series.timestamp), None)

        return target_column

    def _get_last_target_timestamp_from_data_alignment(self, target_column, data_alignment):
        for alignment in data_alignment:
            column_name = alignment.get('column_name')
            timestamp = alignment.get('timestamp')
            if not column_name or not timestamp:  # FIXME remove when request properly validated
                raise ClientValidationError("Invalid 'data_alignment' configuration 'column_name' is missing.")
            if column_name == target_column:
                return pd.to_datetime(timestamp)
        return None

    def _get_last_target_timestamp_from_data(self, target_column, input_time_series: TimeSeries):
        last_valid_index = input_time_series.dataframe[target_column].last_valid_index()
        if last_valid_index is None:
            raise ClientValidationError(f"Target column {target_column} can not have only missing values.")
        return pd.to_datetime(input_time_series.dataframe[input_time_series.timestamp].iloc[last_valid_index])  # FIXME time_series timestamp column type

    def _set_last_target_timestamp(self, input_time_series: TimeSeries):
        target_column = self._get_target_column_name(input_time_series)
        last_target_timestamp = None
        if self._engine_configuration_exists() and 'data_alignment' in self._configuration['engine']:
            last_target_timestamp = self._get_last_target_timestamp_from_data_alignment(target_column, self._configuration['engine']['data_alignment'])
        if last_target_timestamp is None:
            last_target_timestamp = self._get_last_target_timestamp_from_data(target_column, input_time_series)

        self._data_configuration.last_target_timestamp = last_target_timestamp

    def _get_data_alignment(self, input_time_series: TimeSeries):
        timestamp_column = input_time_series.timestamp
        dataframe = input_time_series.dataframe

        data_alignment = self._configuration.get('engine', {}).get('data_alignment', [])

        columns_to_ignore = {timestamp_column}
        columns_to_ignore = columns_to_ignore.union({column_alignment['column_name'] for column_alignment in data_alignment})
        columns_to_add = [col for col in dataframe.columns if col not in columns_to_ignore]
        for col in columns_to_add:
            column_alignment = {}
            last_valid_index = dataframe[col].last_valid_index()
            if last_valid_index:
                column_alignment['column_name'] = col
                column_alignment['timestamp'] = dataframe[timestamp_column][last_valid_index]
            data_alignment.append(column_alignment)

        return data_alignment

    def _arrange_rows(self, rows, sampling_period) -> List[tuple]:
        if rows is None or len(rows) < 2:
            return rows

        sorted_rows = sorted(rows, key=lambda x: x[0])
        correct_rows = [sorted_rows[0]]
        current_start, current_end = sorted_rows[0]

        for start, end in sorted_rows[1:]:
            if end < start:
                continue
            if end > current_end:
                if start <= current_end + sampling_period:
                    correct_rows[-1] = (current_start, end)
                else:
                    current_start = start
                    correct_rows.append((current_start, end))
                current_end = end

        return correct_rows

    def _shift_rows(self, rows: List[tuple], data_depth: pd.offsets.DateOffset) -> List[tuple]:
        output_rows = rows.copy()
        for i, row in enumerate(output_rows):
            output_rows[i] = (row[0] + data_depth, row[-1])

        return output_rows

    def _rows_difference(self, diff_start, diff_end, rows: List[tuple], sampling_period: pd.offsets.DateOffset) -> List[tuple]:
        # assumption rows are sorted and aligned
        if rows is None or len(rows) == 0:
            return (diff_start, diff_end)
        rows_diff = []
        current_start = diff_start
        for start, end in rows:
            if current_start > diff_end:
                break
            if current_start < start:
                rows_diff.append((current_start, min(diff_end, start - sampling_period)))
            current_start = end + sampling_period

        if rows[-1][-1] < diff_end:
            rows_diff.append((current_start, diff_end))

        if len(rows_diff) == 0:
            raise ClientValidationError("Invalid 'out_of_sample_rows' as there are no 'in_sample_rows' remaining.")
        return rows_diff

    def _set_rows(self, input_time_series: TimeSeries):
        sampling_period = input_time_series.sampling_period
        first_timestamp = pd.to_datetime(input_time_series.dataframe[input_time_series.timestamp].iloc[0])
        last_timestamp = self._data_configuration.last_target_timestamp

        self._data_configuration.in_sample_rows = self._arrange_rows(self._data_configuration.in_sample_rows, sampling_period)
        self._data_configuration.out_of_sample_rows = self._arrange_rows(self._data_configuration.out_of_sample_rows, sampling_period)

        if self._data_configuration.in_sample_rows is None:
            if self._data_configuration.out_of_sample_rows is None:
                self._data_configuration.in_sample_rows = [(first_timestamp, last_timestamp)]
            else:
                self._data_configuration.in_sample_rows = self._rows_difference(first_timestamp, last_timestamp, self._data_configuration.out_of_sample_rows, sampling_period)

    def _select_rows(self, input_time_series: TimeSeries, rows: tuple) -> TimeSeries:
        timestamps = pd.to_datetime(input_time_series.dataframe[input_time_series.timestamp])  # FIXME time_series timestamp column type

        mask = np.full(len(timestamps), False, dtype=bool)
        for from_datetime, to_datetime in rows:
            # Filter rows within the current datetime range
            mask |= (timestamps >= from_datetime) & (timestamps <= to_datetime)

        return self._new_time_series(input_time_series.dataframe[mask].reset_index(drop=True))

    def _select_result_rows(self, result_table: pd.DataFrame) -> pd.DataFrame:
        mask = result_table['timestamp'] > self._data_configuration.last_target_timestamp
        for from_datetime, to_datetime in self._data_configuration.out_of_sample_rows:
            # Filter rows within the current datetime range
            mask |= (result_table['timestamp'] >= from_datetime) & (result_table['timestamp'] <= to_datetime)

        return result_table[mask]

    def _get_build_time_series(self, input_time_series: TimeSeries):
        return self._select_rows(input_time_series, self._data_configuration.in_sample_rows)

    def _get_sampling_period_from_model(self):  # FIXME parse model
        value, unit = self._model['model_zoo']['sampling_period'].split(" ")
        return pd.offsets.DateOffset(seconds=int(value)) if unit == "seconds" else pd.offsets.DateOffset(months=int(value))

    def _get_data_depth_from_model(self) -> int:  # FIXME parse model
        variable_properties = self._model['model_zoo']['variable_properties']
        if variable_properties:
            return min(item['data_from'] for item in variable_properties)
        else:
            return 0

    def _get_forecast_rows(self, input_time_series: TimeSeries) -> List[tuple]:
        sampling_period = self._get_sampling_period_from_model()
        data_depth = sampling_period * self._get_data_depth_from_model()
        rows = self._shift_rows(self._data_configuration.out_of_sample_rows, data_depth)
        production_rows_from = self._data_configuration.last_target_timestamp + sampling_period + data_depth
        production_rows_to = pd.to_datetime(input_time_series.dataframe[input_time_series.timestamp].iloc[-1])  # FIXME time_series timestamp column type
        rows.append((production_rows_from, production_rows_to))

        return self._arrange_rows(rows, sampling_period)

    def _get_forecast_series(self, input_time_series: TimeSeries):
        rows = self._get_forecast_rows(input_time_series)
        return self._select_rows(input_time_series, rows)

    def _get_build_configuration(self, input_time_series: TimeSeries):
        if self._engine_configuration_exists():
            build_configuration = self._configuration['engine'].copy()
            build_configuration.pop('prediction_boundaries', None)
        else:
            build_configuration = {}

        build_configuration['data_alignment'] = self._get_data_alignment(input_time_series)

        return build_configuration

    def _get_forecast_configuration(self):
        if self._engine_configuration_exists():
            config = self._configuration['engine']
            keys_to_select = ['prediction_from', 'prediction_to', 'prediction_boundaries', 'data_alignment']
            return {key: config[key] for key in keys_to_select if key in config}
        else:
            return {}

    def _engine_configuration_exists(self):
        return (self._configuration is not None and
                'engine' in self._configuration and
                isinstance(self._configuration['engine'], dict))

    def _new_time_series(self, dataframe: pd.DataFrame):
        return TimeSeries(self._license, dataframe, self._time_series.timestamp, self._time_series.timestamp_format)
