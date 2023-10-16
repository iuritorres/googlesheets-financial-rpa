import enum

class GSheetsPermissionLevel(enum.StrEnum):
    WRITE = 'https://www.googleapis.com/auth/spreadsheets'
    READ_ONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly'
