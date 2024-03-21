"""Excel class."""
import requests
from O365 import Account

from t_office_365.decorators import retry_if_exception
from t_office_365.endpoints import ExcelEndpoints
from t_office_365.utils import check_result


class Excel:
    """Excel class is used for API calls to Excel."""

    def __init__(self, account: Account, drive_id: str) -> None:
        """
        Initializes an instance of the Excel class.

        :param:
        - account (O365.Account): The O365 Account used for authentication.
        - drive_id (str): The ID of the drive.
        """
        self.endpoints = ExcelEndpoints(account, drive_id)

    @retry_if_exception
    def get_sheet_names(self, file_id: str) -> dict:
        """
        Get sheet names from Excel file.

        :param:
        - file_id (str): The ID of the Excel file.

        :return:
            dict: The sheet names json.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = f"{self.endpoints.base_url}/drivses/{self.endpoints.drive_id}/items/{file_id}/workbook/worksheets"
        result = requests.get(url, headers=self.endpoints.headers)
        check_result(result, f"{file_id}")
        return result.json()

    @retry_if_exception
    def create_sheet(self, file_id, sheet_name) -> None:
        """
        Create a new sheet in Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the new sheet.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = f"{self.endpoints.base_url}/drives/{self.endpoints.drive_id}/items/{file_id}/workbook/worksheets"
        payload = {"name": sheet_name}
        result = requests.post(url, json=payload, headers=self.endpoints.headers)
        check_result(result, f"{file_id}")

    @retry_if_exception
    def get_rows(self, file_id: str, sheet_name: str, last_row: str) -> dict:
        """
        Get rows data from Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - last_row (int): The index of the last row to retrieve.


        :return:
            dict: The rows json.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = self.endpoints.get_rows_data.format(file_id=file_id, sheet_name=sheet_name, last_row=last_row)
        result = requests.get(url, headers=self.endpoints.headers)
        check_result(result, f"{file_id}")
        return result.json()

    @retry_if_exception
    def update_cell_value(self, file_id, sheet_name, row, column, value) -> None:
        """
        Update cell value in Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - row (int): The row index of the cell.
        - column (int): The column index of the cell.
        - value: The new value to be set in the cell.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = self.endpoints.update_excel_endpoint.format(
            file_id=file_id, sheet_name=sheet_name, row=row, column=column
        )
        payload = {"values": [[value]]}
        result = requests.patch(url, json=payload, headers=self.endpoints.headers)
        check_result(result, f"{file_id}")

    @retry_if_exception
    def update_row_values(self, file_id, sheet_name, address, values) -> None:
        """
        Update row values in Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - address (str): The address of the row to update.
        - values: The new values to be set in the row.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = self.endpoints.update_row_data.format(file_id=file_id, sheet_name=sheet_name, address=address)
        payload = {"values": [values]}
        result = requests.patch(url, json=payload, headers=self.endpoints.headers)
        check_result(result, f"{file_id}")
