from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheet:
	def __init__(self, spreadsheet_id: str, scopes: list[str]) -> None:
		self.__credentials = None
		self.spreadsheet_id = spreadsheet_id
		self.SCOPES = scopes
		self.sheet = None

		self.authenticate()
		self.init_spreadsheet()


	def authenticate(self):
		if os.path.exists('token.json'):
			self.__credentials = Credentials.from_authorized_user_file('token.json', self.SCOPES)

		if not self.__credentials or not self.__credentials.valid:
			if self.__credentials and self.__credentials.expired and self.__credentials.refresh_token:
				self.__credentials.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(
					'credentials.json', self.SCOPES)
				self.__credentials = flow.run_local_server(port = 0)

			with open('token.json', 'w') as token:
				token.write(self.__credentials.to_json())


	def init_spreadsheet(self):
		try:
			service = build('sheets', 'v4', credentials = self.__credentials)

			# Call the Sheets API
			self.sheet = service.spreadsheets()

		except HttpError as error:
			print(error)


	def read(self, range_name: str) -> list[list]:
		return self.sheet.values().get(
			spreadsheetId = self.spreadsheet_id,
			range = range_name
		).execute()


	def write(self, range_name: str) -> None:
		return self.sheet.values().update(
			spreadsheetId = self.spreadsheet_id,
			range = range_name
		).execute()
