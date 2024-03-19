"""
Microsoft Graph API Endpoints for Excel, OneDrive, and SharePoint.

This module defines classes for managing Microsoft Graph API endpoints related to Excel, OneDrive, and SharePoint.
The classes provide a structured interface for interacting with Microsoft services using the O365 library.

Classes:
- BaseEndpoints: Base class containing common attributes and methods for API endpoints.
- ExcelEndpoints: Subclass of BaseEndpoints for managing OfficeAccount Excel-related operations.
- OnedriveEndpoints: Subclass of BaseEndpoints for managing OfficeAccount OneDrive-related operations.
- SharepointEndpoints: Subclass of BaseEndpoints for managing OfficeAccount SharePoint-related operations.
"""

from dataclasses import dataclass
from urllib.parse import quote

from O365 import Account

from t_office_365.constants import MS_GRAPH_BASE_URL


@dataclass
class BaseEndpoints:
    """
    Initializes BaseEndpoints with the provided O365 Account.

    :param:
    - account (O365.Account): The O365 Account used for authentication.
    - base_url (str, optional): The base URL for Microsoft Graph API.

    :return:
    - None
    """

    account: Account
    base_url: str = MS_GRAPH_BASE_URL

    @property
    def file_chunk_size(self) -> int:
        """The size of file chunks for uploading in bytes."""
        return 10485760

    @property
    def access_token(self):
        """Get the access token from the account."""
        return self.account.con.session.access_token

    @property
    def expiration_datetime(self):
        """Get the expiration datetime of the token."""
        return self.account.connection.token_backend.token.expiration_datetime

    @property
    def headers(self):
        """Get the headers for the request."""
        return {"Authorization": f"Bearer {self.access_token}"}

    @staticmethod
    def encode_url(url) -> str:
        """Encode the url."""
        return quote(url)


class DriveBasedEndpoints(BaseEndpoints):
    """Subclass of BaseEndpoints for managing OfficeAccount's Drive ID related operations."""

    def __init__(
        self,
        account: Account,
        drive_id: str,
        base_url: str = MS_GRAPH_BASE_URL,
    ):
        """
        Initializes DriveBasedEndpoints with the provided O365 Account and Drive ID.

        :param:
        - account (O365.Account): The O365 Account used for authentication.
        - drive_id (str, optional): The ID of the drive.
        - base_url (str, optional): The base URL for Microsoft Graph API.

        :return:
        - None
        """
        super().__init__(account, base_url)
        self.drive_id = drive_id


class ExcelEndpoints(DriveBasedEndpoints):
    """Subclass of DriveBasedEndpoints for managing OfficeAccount Excel-related operations."""

    @property
    def update_excel_endpoint(self):
        """Update excel endpoint field.

        Returns:
            str: update excel endpoint
        """
        return (
            f"{self.base_url}/drives/{self.drive_id}/items/"
            + "{file_id}/workbook/worksheets/{sheet_name}/cell(row={row}, column={column})"
        )

    @property
    def get_rows_data(self):
        """Get row data field.

        Returns:
            str: get row data
        """
        return (
            f"{self.base_url}/drives/{self.drive_id}/items/"
            + "{file_id}/workbook/worksheets/{sheet_name}/range(address='A1:ZZ{last_row}')"
        )

    @property
    def update_row_data(self):
        """Update row data.

        Returns:
            str: get row data
        """
        return (
            f"{self.base_url}/drives/{self.drive_id}/items/"
            + "{file_id}/workbook/worksheets/{sheet_name}/range(address='{address}')"
        )


class OnedriveEndpoints(DriveBasedEndpoints):
    """Subclass of DriveBasedEndpoints for managing OfficeAccount OneDrive-related operations."""


class OutlookEndpoints(BaseEndpoints):
    """Subclass of BaseEndpoints for managing OfficeAccount Outlook-related operations."""

    @property
    def new_message(self):
        """Get the mailbox of the account."""
        return self.account.new_message()

    @property
    def mailbox(self):
        """Get the mailbox of the account."""
        return self.account.mailbox()

    @property
    def inbox_folder(self):
        """Get the inbox folder of the mailbox."""
        return self.mailbox.inbox_folder()

    @property
    def archive_folder(self):
        """Get the archive folder of the mailbox."""
        return self.mailbox.archive_folder()

    @property
    def mail_main_endpoint(self) -> str:
        """Get the main endpoint for the email."""
        return f"{self.base_url}/{self.mailbox.main_resource}"

    @property
    def mail_child_folders_endpoint(self) -> str:
        """Get the endpoint to get the child folders of a mail folder."""
        return f"{self.mail_main_endpoint}" + "/mailFolders/{folder_id}/childFolders"

    @property
    def get_messages_from_folder_endpoint(self):
        """Get the endpoint to get the messages from a mail folder."""
        return f"{self.mail_main_endpoint}" + "/mailFolders/{folder_id}/messages"


class SharepointEndpoints(DriveBasedEndpoints):
    """Subclass of DriveBasedEndpoints for managing OfficeAccount Sharepoint-related operations."""

    @property
    def folder_id_endpoint(self) -> str:
        """Get the endpoint to get the folder id."""
        return f"{self.base_url}/drives/{self.drive_id}" + "/root:/{folder_path}"

    @property
    def folder_items_endpoint(self) -> str:
        """Get the endpoint to get the items of a folder."""
        return f"{self.base_url}/drives/{self.drive_id}" + "/items/{folder_id}/children"

    @property
    def file_content_endpoint(self) -> str:
        """Get the endpoint to get the content of a file."""
        return f"{self.base_url}/drives/{self.drive_id}" + "/items/{file_id}/content"

    @property
    def file_info_endpoint(self) -> str:
        """Get the endpoint to get the info of a file."""
        return f"{self.base_url}/drives/{self.drive_id}" + "/root:/{file_path}"

    @property
    def file_upload_session_endpoint(self) -> str:
        """Get the endpoint to create an upload session."""
        return f"{self.base_url}/drives/{self.drive_id}" + "/items/{folder_id}:/{file_url}:/createUploadSession"

    @property
    def file_content_by_url_endpoint(self) -> str:
        """Get the endpoint to get the content of a file by url."""
        return f"{self.base_url}/drives/{self.drive_id}" + "/items/{folder_id}:/{file_url}:/content"

    @property
    def file_id_endpoint(self):
        return f"{self.base_url}/drives/{self.drive_id}" + "/items/{file_id}"
