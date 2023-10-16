from enum import StrEnum

class GSheetsPermissionLevel(StrEnum):
    WRITE = 'https://www.googleapis.com/auth/spreadsheets'
    READ_ONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly'
