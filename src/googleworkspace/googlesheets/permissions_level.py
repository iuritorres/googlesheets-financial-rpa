"""Module that provides a class with google sheets permissions levels."""
from dataclasses import dataclass

@dataclass
class GSheetsPermissionLevel:
    """https://developers.google.com/sheets/api/quickstart/python?hl=pt-br#configure_the_sample"""

    WRITE = 'https://www.googleapis.com/auth/spreadsheets'
    READ_ONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly'
