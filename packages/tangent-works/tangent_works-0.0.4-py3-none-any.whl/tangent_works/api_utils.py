import requests

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
