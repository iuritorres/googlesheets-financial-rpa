# Python native modules
from __future__ import print_function
import os.path
from json import loads as to_json

# External libs/services
from apiclient import discovery
from google.oauth2 import service_account
from googleapiclient.errors import HttpError

from dotenv import load_dotenv; load_dotenv()

# Project
from GSheetsPermissionLevel import GSheetsPermissionLevel


class GoogleSheet:
	def __init__(self, spreadsheet_id: str, permission_level: GSheetsPermissionLevel) -> None:
		self.__credentials = None
		self.__sheet = None
		self.spreadsheet_id = spreadsheet_id
		self.SCOPES = [permission_level]

		self.authenticate()
		self.init_spreadsheet()


	def authenticate(self):
		try:
			print(os.environ['GOOGLE_CREDENTIALS'])
			google_credentials = to_json(os.getenv('GOOGLE_CREDENTIALS'))
			self.__credentials = service_account.Credentials.from_service_account_info(google_credentials)

		except HttpError as error:
			print(error)


	def init_spreadsheet(self):
		try:
			service = discovery.build('sheets', 'v4', credentials=self.__credentials)

			self.__sheet = service.spreadsheets()

		except HttpError as error:
			print(error)


	def read(self, range_name: str) -> list[list]:
		return self.__sheet.values().get(
			spreadsheetId = self.spreadsheet_id,
			range = range_name
		).execute()


	def write(self, range_name: str) -> None:
		return self.__sheet.values().update(
			spreadsheetId = self.spreadsheet_id,
			range = range_name
		).execute()
