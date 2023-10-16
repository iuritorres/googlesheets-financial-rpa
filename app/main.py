# from dotenv import load_dotenv; load_dotenv()
import os.path

# from GoogleSheet import GoogleSheet
# from GSheetsPermissionLevel import GSheetsPermissionLevel

SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'

# sheet = GoogleSheet(
#     spreadsheet_id = SPREADSHEET_ID,
#     permission_level= GSheetsPermissionLevel.WRITE
# )

print(os.getenv('TESTEE'))
