from GoogleSheet import GoogleSheet

SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
sheet = GoogleSheet(
    spreadsheet_id = SPREADSHEET_ID,
    scopes = SCOPES
)
