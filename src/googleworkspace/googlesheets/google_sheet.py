"""Module that provides a class for Google Sheets spreadsheets."""
from __future__ import print_function
from json import loads as to_json
import os.path

from apiclient import discovery
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

from googleworkspace.googlesheets.permissions_level import GSheetsPermissionLevel

load_dotenv()


class GoogleSheet:
    """Class that integrates with Google Sheets."""

    def __init__(self, spreadsheet_id: str, permission_level: GSheetsPermissionLevel) -> None:
        self.__credentials = None
        self.__sheet = None
        self.spreadsheet_id = spreadsheet_id
        self.scopes = [permission_level]

        self.authenticate()
        self.init_spreadsheet()

    def authenticate(self):
        """Connect to Google's OAuth2 API."""
        try:
            google_credentials = to_json(os.getenv('GOOGLE_CREDENTIALS'))
            self.__credentials = service_account.Credentials.from_service_account_info(
                google_credentials)

        except HttpError as error:
            print(error)

    def init_spreadsheet(self):
        """Get and save spreadsheet."""
        try:
            service = discovery.build(
                'sheets', 'v4', credentials=self.__credentials)

            self.__sheet = service.spreadsheets()  # pylint: disable=no-member

        except HttpError as error:
            print(error)

    def read(self, range_name: str) -> list[list]:
        """Simplified way to read spreadsheet data."""
        return self.__sheet.values().get(
            spreadsheetId=self.spreadsheet_id,
            range=range_name
        ).execute()

    def write(self, range_name: str) -> None:
        """Simplified way to write data in spreadsheet."""
        return self.__sheet.values().update(
            spreadsheetId=self.spreadsheet_id,
            range=range_name
        ).execute()
