"""Utility functions."""
import os

from t_office_365.exceptions import (
    BadRequestError,
    UnexpectedError,
    AuthenticationGraphError,
    AssetLockedError,
    AssetNotFoundError,
    ServiceUnavailableError,
)


def check_path(path: str) -> None:
    """
    Check if the given path exists as a directory.

    :param:
        - path (str): The path to be checked.

    :raise:
        AssetNotFoundError: If the path does not exist as a directory.
    """
    if not os.path.isdir(path):
        raise AssetNotFoundError(f"No such directory: '{path}'")


def check_result(result, asset: str = "") -> None:
    """
    Checks the HTTP status code of a request result and raises specific exceptions based on common error codes.

    :param:
    - result: The result of an HTTP request (response object).
    - asset: Optional. The asset associated with the request, used for error messages.

    :raises:
     - AuthenticationGraphError: If the status code is 401.
     - AssetLockedError: If the status code is 423, with a message indicating the asset is locked.
     - BadRequestError: If the status code is 400, with a message indicating processing failure for the asset.
     - AssetNotFoundError: If the status code is 404, with a message indicating the asset was not found.
     - ServiceUnavailableError: If the status code is 503.
     - UnexpectedError: If the status code is not 200, with a generic error message.
    """
    status_code = result.status_code
    error = result.json().get("error", None)
    error_message = None

    if error is not None:
        error_message = error.get("message", None)

    status_code_exceptions_map = {
        401: AuthenticationGraphError(error_message),
        423: AssetLockedError(f"Asset '{asset}' locked!"),
        400: BadRequestError(f"Unable to process: '{asset}'"),
        404: AssetNotFoundError(f"Asset '{asset}' not found!"),
        503: ServiceUnavailableError(error_message),
    }
    ex = status_code_exceptions_map.get(status_code, None)
    if ex:
        raise ex
    if status_code != 200:
        raise UnexpectedError(f'An unexpected error while processing asset "{asset}". (Status code {status_code})')
