"""SharePoint class."""
import os
from abc import ABC

import requests
from O365 import Account

from t_office_365.constants import FILE_CHUNK_SIZE
from t_office_365.decorators import retry_if_exception
from t_office_365.drive.drive import Drive, DriveSite
from t_office_365.endpoints import drive_api
from t_office_365.exceptions import AssetNotFoundError, BadRequestError
from t_office_365.utils import check_result


class SharepointSite(DriveSite, ABC):
    """Represents a SharePoint site in Microsoft Office 365.

    Provides access to SharePoint-specific services and Excel functionality.
    """

    def __init__(self, account: Account, site_name: str) -> None:
        """Initializes instance of the SharepointService class.

        :param:
        - account: The account object containing the authentication information.
        - site_name: The name of microsoft office site.
        """
        self.__site_name = site_name
        super().__init__(account)

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

    @retry_if_exception
    def download_file_by_id(self, file_id: str, file_name: str = None, target_folder: str = os.getcwd()) -> str:
        """Download a file from SharePoint with file ID and save it to the target folder.

        :param:
        - file_id: The ID of file which want to download.
        - file_name : The name to be used which saving the downloaded file.
        - target_folder : The folder where the file should be saved.

        :return:
        - The file path of the to be downloaded.

        :return:
        The full path to the downloaded file.
        """
        return self.__download_file(file_id, file_name, target_folder)

    @retry_if_exception
    def does_file_exists_by_path(self, file_path: str) -> bool:
        """Check if a file exists in SharePoint.

        :param:
        - file_path (str): The path to the file which should be checked.

        :return:
        - bool: True if the file exists, False otherwise.
        """
        try:
            folder_id = self.__get_folder_id(os.path.dirname(file_path))
            self.__check_file_exist(folder_id, os.path.basename(file_path))
        except (AssetNotFoundError, BadRequestError):
            return False
        return True

    @retry_if_exception
    def does_file_exists_by_id(self, file_id: str) -> bool:
        """Check if a file exists in SharePoint based on file ID.

        :param:
         - file_id (str):The ID of the file.

        :return: bool
            True if the file exists, False otherwise.

        :raises BadRequestError:
            If there is an issue with the request.
        """
        url = self.get_url(drive_api.file_id_endpoint(self.drive_id, file_id))
        result = requests.get(url, headers=self.headers())
        try:
            check_result(result, file_id)
        except (BadRequestError, AssetNotFoundError):
            return False
        return True

    @retry_if_exception
    def upload_file(self, file_path: str, folder_path: str) -> None:
        """Uploads a file to SharePoint, with handling both small and large uploads.

        :param:
        - file_path (str): The file path to be uploaded.
        - folder_path (str): The SharePoint folder path where the file should be uploaded.
        """
        st = os.stat(file_path)
        size = st.st_size
        folder_id = self.__get_folder_id(folder_path)
        path_url = self.encode_url(os.path.join(folder_path, os.path.basename(file_path)))
        if size / (1024 * 1024) < 4:
            url = self.get_url(drive_api.file_info_endpoint(self.drive_id, path_url))
            result = requests.get(url, headers=self.headers())
            try:
                check_result(result, file_path)
                file_info = result.json()
                self.__upload_existing_file_by_id(file_path, file_info["id"])
            except AssetNotFoundError:
                # file does not exist, create a new item
                self.__upload_not_existing_file_by_folder_id(file_path, os.path.basename(file_path), folder_id)
        else:
            self.__upload_large_file(file_path, os.path.basename(file_path), folder_id, size)

    @retry_if_exception
    def delete_file(self, file_id: str) -> None:
        """Delete a file from the drive by file id.

        :param:
        - file_id (str): The ID of the file to be deleted.
        """
        url = self.get_url(drive_api.file_id_endpoint(self.drive_id, file_id))
        result = requests.delete(url, headers=self.headers())
        check_result(result, file_id)

    @retry_if_exception
    def get_or_create_folder(self, folder_path: str):
        """Get or create a folder on SharePoint.

        :param:
        - file_path: The file path used to derive the SharePoint folder path.

        :return:
        - The ID of the existing or newly created folder.

        :raises:
        - AssetNotFoundError: If there is an error during the folder retrieval.
        """
        try:
            folder_id = self.__get_folder_id(folder_path)
            return folder_id
        except AssetNotFoundError:
            folder_data = {
                "name": os.path.basename(folder_path),
                "folder": {},
                "@microsoft.graph.conflictBehavior": "rename",
            }
            folder_id = self.__get_folder_id(os.path.dirname(folder_path))
            url = self.get_url(drive_api.folder_items_endpoint(self.drive_id, folder_id))
            result = requests.post(url, self.headers({"Content-type": "application/json"}), json=folder_data)
            check_result(result, folder_path)

    @retry_if_exception
    def get_folder_contents_by_path(self, folder_path: str) -> str:
        """Get folder contents by path from SharePoint and download a specific file if found.

        :param:
        - folder_items_endpoint (str): The endpoint for retrieving folder items.
        - file_name (str): The name of the file to be searched and downloaded.
        - target_folder (str): The local directory where the file should be downloaded.

        :return:
        - The folder contents.
        """
        folder_id = self.__get_folder_id(folder_path)
        return self.__get_folder_contents(folder_id)

    @retry_if_exception
    def get_folder_contents_by_id(self, folder_id: str) -> str:
        """Get folder contents by id from SharePoint and download a specific file if found.

        :param:
        - folder_items_endpoint (str): The endpoint for retrieving folder items.
        - file_name (str): The name of the file to be searched and downloaded.
        - target_folder (str): The local directory where the file should be downloaded.

        :return:
        - The folder contents.
        """
        return self.__get_folder_contents(folder_id)

    def _get_drive_id(self) -> str:
        """Get the Drive ID for SharePoint.

        :param:
        - site_name (str): The name of the site.

        :return:
        - str: The ID of the SharePoint Drive.
        """
        site_id = self.account.sharepoint().get_site("root", self.__site_name).object_id

        url = self.get_url(f"/sites/{site_id}/drive")
        result = requests.get(url, headers=self.headers())
        check_result(result, url)
        return result.json()["id"]

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

    def __get_folder_contents(self, folder_id: str) -> str:
        """Get folder contents from SharePoint and download a specific file if found.

        :param:
        - folder_id (str): The ID of the SharePoint folder.

        :return:
        - The folder contents.
        """
        url = self.get_url(drive_api.folder_items_endpoint(self.drive_id, folder_id))
        result = requests.get(url, headers=self.headers())
        check_result(result, folder_id)
        return result.json()["value"]

    def __check_file_exist(self, folder_id: str, file_name: str) -> None:
        """Check if a file exists in a SharePoint folder.

        :param:
        - folder_items_endpoint (str): The endpoint URL for retrieving folder items in SharePoint.
        - file_name (str): The name of the file to check for existence.

        :return:
        - bool: True if the file exists, False otherwise.

        :raise:
        - AssetNotFoundError: if the file does not exist on SharePoint.
        """
        url = self.get_url(drive_api.folder_items_endpoint(self.drive_id, folder_id))
        result = requests.get(url, headers=self.headers())
        check_result(result, file_name)
        children = result.json()["value"]
        for item in children:
            if str(item["name"]).lower() == file_name.lower():
                return
        else:
            raise AssetNotFoundError(f"'{file_name}' not found!")

    def __upload_existing_file_by_id(self, file_path: str, file_id: str) -> None:
        """Uploads an existing file to SharePoint with file id.

        :param:
        - file_path (str): The file path of the existing file to be uploaded.
        - file_id (str): The SharePoint file to which the upload will be performed.

        :raise:
        - If the file is locked on the SharePoint.
        """
        url = self.get_url(drive_api.file_content_endpoint(self.drive_id, file_id))
        result = requests.put(
            url,
            headers=self.headers({"Content-type": "application/binary"}),
            data=open(file_path, "rb").read(),
        )
        check_result(result, f"{file_path}/{file_id}")

    def __upload_not_existing_file_by_folder_id(self, file_path: str, file_name: str, folder_id: str) -> None:
        """Uploads a file to SharePoint within a specified folder using the folder.

        :param:
        - file_path (str): The  file path of the file to be uploaded.
        - file_name (str): The name of the file to be uploaded.
        - folder_id (str): The SharePoint  folder where the file will be uploaded.

        :raise:
        - If there is an error uploading the file to the SharePoint
        """
        url = self.get_url(drive_api.file_content_by_url_endpoint(self.drive_id, folder_id, self.encode_url(file_name)))
        result = requests.put(
            url,
            headers=self.headers({"Content-type": "application/binary"}),
            data=open(file_path, "rb").read(),
        )
        check_result(result, file_name)

    def __upload_large_file(self, file_path: str, file_name: str, folder_id: str, size: int) -> None:
        """Uploads a large file to SharePoint using the Microsoft Graph api resumable upload session.

        :param:
        - file_path (str): The file path of the large file to be uploaded.
        - file_name (str): The name to be assigned to the file on SharePoint.
        - folder_id (str): The SharePoint folder where the file will be uploaded.
        - size (int): The size of the file in bytes.

        :raise:
        - If there is an error while Uploading the large file.
        """
        url = self.get_url(drive_api.file_upload_session_endpoint(self.drive_id, folder_id, self.encode_url(file_name)))
        data = {
            "@microsoft.graph.conflictBehavior": "replace",
            "description": "A large file",
            "fileSystemInfo": {"@odata.type": "microsoft.graph.fileSystemInfo"},
            "name": file_path,
        }
        result = requests.post(url, headers=self.headers(), json=data)
        check_result(result)
        upload_url = result.json()["uploadUrl"]

        chunks = int(size / FILE_CHUNK_SIZE) + 1 if size % FILE_CHUNK_SIZE > 0 else 0
        with open(file_path, "rb") as fd:
            start = 0
            for chunk_num in range(chunks):
                chunk = fd.read(FILE_CHUNK_SIZE)
                bytes_read = len(chunk)
                upload_range = f"bytes {start}-{start + bytes_read - 1}/{size}"
                upload_result = requests.put(
                    upload_url, headers={"Content-Length": str(bytes_read), "Content-Range": upload_range}, data=chunk
                )
                check_result(upload_result, upload_url)
                start += bytes_read


class Sharepoint(Drive):
    """SharePoint class is used for API calls to SharePoint."""

    def site(self, site_name: str) -> SharepointSite:
        """Get a SharePoint site by its name.

        :param:
        - site_name: The name of the SharePoint site.

        :return:
        - A SharepointSite object representing the specified SharePoint site.
        """
        return SharepointSite(self.account, site_name)
