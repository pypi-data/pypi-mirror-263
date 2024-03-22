"""Excel class."""
from typing import List

import requests
from O365 import Account

from t_office_365.core import Core
from t_office_365.decorators import retry_if_exception
from t_office_365.endpoints import workbook_api
from t_office_365.utils import check_result


class Excel(Core):
    """Excel class is used for API calls to Excel."""

    def __init__(self, account: Account, drive_id: str) -> None:
        """Initializes an instance of the Excel class.

        :param:
        - account (O365.Account): The O365 Account used for authentication.
        - drive_id (str): The ID of the drive.
        """
        super().__init__(account)
        self.__drive_id = drive_id

    @retry_if_exception
    def get_sheet_names(self, file_id: str) -> dict:
        """Get sheet names from Excel file.

        :param:
        - file_id (str): The ID of the Excel file.

        :return:
            dict: The sheet names json.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = self.get_url(workbook_api.worksheets(self.__drive_id, file_id))
        result = requests.get(url, headers=self.headers())
        check_result(result, f"{file_id}")
        return result.json()

    @retry_if_exception
    def create_sheet(self, file_id, sheet_name) -> None:
        """Create a new sheet in Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the new sheet.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = self.get_url(workbook_api.worksheets(self.__drive_id, file_id))
        payload = {"name": sheet_name}
        result = requests.post(url, json=payload, headers=self.headers())
        check_result(result, f"{file_id}")

    @retry_if_exception
    def get_rows_values(
        self, file_id: str, sheet_name: str, max_row: int = 100, max_column: int = 26
    ) -> List[List[str]]:
        """Get rows values from Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - max_row (int): The index of the last row to retrieve.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        result = self.get_rows_range_data(file_id, sheet_name, max_row, max_column)
        return result["values"]

    @retry_if_exception
    def get_rows_range_data(self, file_id: str, sheet_name: str, max_row: int = 100, max_column: int = 26) -> dict:
        """Get rows range data from Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - max_row (int, optional): The index of the last row to retrieve.
        - max_column (int, optional): The index of the column to retrieve.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        col_letter = self.__get_column_letter(max_column)

        url = self.get_url(workbook_api.get_row_data(self.__drive_id, file_id, sheet_name, max_row, col_letter))
        result = requests.get(url, headers=self.headers())
        check_result(result, f"{file_id}")
        return result.json()

    @retry_if_exception
    def get_row_values(self, file_id: str, sheet_name: str, row: int, max_column: int) -> List[List[str]]:
        """Get rows values from Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - row (int):
        - max_column (str):

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        col_letter = self.__get_column_letter(max_column)
        url = self.get_url(workbook_api.get_specific_row(self.__drive_id, file_id, sheet_name, row, col_letter))
        result = requests.get(url, headers=self.headers())
        check_result(result, f"{file_id}")
        return result.json()["values"]

    @retry_if_exception
    def get_cell_value(self, file_id: str, sheet_name: str, row: int, column: int) -> List[List[str]]:
        """Get cell value from Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - row (int): The row index of the cell.
        - column (int): The column index of the cell.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = self.get_url(workbook_api.get_cell_value(self.__drive_id, file_id, sheet_name, row, column))
        result = requests.get(url, headers=self.headers())
        check_result(result, f"{file_id}")
        return result.json()["values"]

    @retry_if_exception
    def update_cell_value(self, file_id, sheet_name, row, column, value) -> None:
        """Update cell value in Excel.

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
        url = workbook_api.get_cell_value(self.__drive_id, file_id, sheet_name, row, column)
        payload = {"values": [[value]]}
        result = requests.patch(url, json=payload, headers=self.headers())
        check_result(result, f"{file_id}")

    @retry_if_exception
    def update_row_values(self, file_id, sheet_name, address, values) -> None:
        """Update row values in Excel.

        :param:
        - file_id (str): The ID of the Excel file.
        - sheet_name (str): The name of the sheet.
        - address (str): The address of the row to update.
        - values: The new values to be set in the row.

        :raises:
        - BadRequestError: If there is a bad request.
        - UnexpectedError: If there is an unexpected error during the request.
        """
        url = workbook_api.update_row_data(self.__drive_id, file_id, sheet_name, address)
        payload = {"values": [values]}
        result = requests.patch(url, json=payload, headers=self.headers())
        check_result(result, f"{file_id}")

    @staticmethod
    def __get_column_letter(column_int: int) -> str:
        """Get column letter."""
        if column_int < 1 or column_int > 702:
            raise ValueError("Column number must be greater than 0 and less than 703.")
        start_index = 1  # it can start either at 0 or at 1
        letter = ""
        while column_int > 25 + start_index:
            letter += chr(65 + int((column_int - start_index) / 26) - 1)
            column_int = column_int - (int((column_int - start_index) / 26)) * 26
        letter += chr(65 - start_index + (int(column_int)))
        return letter
