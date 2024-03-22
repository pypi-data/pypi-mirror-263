import io
import requests
import pandas as pd

from .exceptions import APIError


def raise_on_error_response(response: requests.Response) -> None:
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        response_status_code = response.status_code

        try:
            response_error_message = response.json()['message']
        except:
            response_error_message = f'API error: {response.text}'

        exception_message = f'{response_error_message} (HTTP {response_status_code})'
        raise APIError(exception_message) from err


def create_authorization_header(token: str) -> dict[str, str]:
    return {
        'Authorization': f'Bearer {token}'
    }


def csv_request_part(part_name: str, part_value: str) -> tuple[str, tuple[str, str, str]]:
    return (part_name, (f'{part_name}.csv', part_value, 'text/csv'))


def json_request_part(part_name: str, part_value: str) -> tuple[str, tuple[str, str, str]]:
    return (part_name, (f'{part_name}.json', part_value, 'application/json'))


def response_to_dataframe(response: requests.Response, timestamp_columns: list[str]):
    return pd.read_csv(io.StringIO(response.text), sep=None, parse_dates=timestamp_columns)
