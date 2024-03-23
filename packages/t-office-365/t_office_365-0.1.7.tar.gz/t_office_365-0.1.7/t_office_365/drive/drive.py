"""Drive class for managing OneDrive and Sharepoint API calls."""
import os
import re
from abc import abstractmethod

import requests
from O365 import Account

from t_office_365.core import Core
from t_office_365.decorators import retry_if_exception
from t_office_365.drive.excel import Excel
from t_office_365.endpoints import drive_api
from t_office_365.utils import check_result, get_validated_target_folder


class Drive(Core):
    """Main Drive class."""

    @abstractmethod
    def site(self, *args, **kwargs):
        """Get the drive ID for the site."""
        raise NotImplementedError

    def get_available_sites(self) -> list:
        """Get a list of existing sites.

        :return:
        - list of sites
        """
        result = requests.get(self.get_url("/sites?search=*"), headers=self.headers())
        check_result(result, "Sites")
        return result.json()["value"]


class DriveSite(Core):
    """DriveSite class is used for API calls to OneDrive and Sharepoint."""

    def __init__(self, account: Account) -> None:
        """Initializes an instance of the Drive class.

        :param:
        - account: The account object containing the authentication information.
        """
        super().__init__(account)
        self.__drive_id = self._get_drive_id()
        self.__excel_instance = None

    @abstractmethod
    def _get_drive_id(self) -> str:
        """Get the drive ID for the site."""
        raise NotImplementedError

    @property
    def drive_id(self):
        """Property for accessing the drive ID."""
        if not self.__drive_id:
            self.__drive_id = self._get_drive_id()
        return self.__drive_id

    @property
    def excel(self) -> Excel:
        """Property for accessing the Excel service.

        :return:
        Excel: An instance of the Excel class for managing Excel-related operations.
        """
        if self.__excel_instance is None:
            self.__excel_instance = Excel(self.account, self.drive_id)
        return self.__excel_instance

    @retry_if_exception
    def get_file_id_by_path(self, file_path: str) -> str:
        """Get the file ID.

        :param:
        - file_path (str): The file path for retrieving file information.

        :return:
        - str: The ID of the file.

        :raise:
        - If there is an error during the file ID retrieval.
        """
        return self.__get_folder_id(file_path)

    @retry_if_exception
    def download_file_by_path(self, file_path: str, file_name: str = None, target_folder: str = os.getcwd()) -> str:
        """Download a file from SharePoint to the specified target folder.

        :param:
        - file_path (str): The path to the file to be downloaded.
        - target_folder (str): The path to the folder where the file should be downloaded.

        :return:
        - str: The path to the file to be downloaded

        :raise:
        - If there is an issue with file path which is downloaded.
        """
        file_id = self.__get_folder_id(file_path)
        return self.__download_file(file_id, file_name, target_folder)

    def __get_folder_id(self, folder_path: str) -> str:
        """Get the Folder ID from SharePoint.

        :param:
        - folder_path (str): The folder path for retrieving folder information.

        :return:
        - str: The ID of the SharePoint folder.

        :raise:
        - If there is an error during the Folder ID retrieval.
        """
        url = self.get_url(drive_api.folder_id_endpoint(self.drive_id, self.encode_url(folder_path)))
        result = requests.get(url, headers=self.headers())
        check_result(result, f"{folder_path}")
        return result.json()["id"]

    def __download_file(self, file_id: str, file_name: str, target_folder: str) -> str:
        """Download a file from SharePoint.

        :param:
        - file_id (str): The ID of the file to be downloaded.
        - file_name(str): The name of the file to be used when saving locally.
        - target_folder(str): The local directory where the file should be downloaded.

        :return:
        - The local file path where the downloaded file is saved.
        """
        # check_path(target_folder)
        target_folder = get_validated_target_folder(target_folder)
        url = self.get_url(drive_api.file_content_endpoint(self.drive_id, file_id))
        result = requests.get(url, headers=self.headers())
        check_result(result, file_id)

        file_name = (
            file_name if file_name else re.findall("filename=(.+)", result.headers["Content-Disposition"])[0][1:-1]
        )

        file_path = os.path.join(target_folder, file_name)
        with open(file_path, "wb") as w:
            w.write(result.content)
        return f"{file_path}"
