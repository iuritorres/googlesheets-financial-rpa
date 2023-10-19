# GHACTIONS - ModuleNotFoundError: No module named (Any library)
import pandas as pd

from GoogleSheet import GoogleSheet
from GSheetsPermissionLevel import GSheetsPermissionLevel

import os.path

# sheet = GoogleSheet(
#     spreadsheet_id = '16tfSBgIJusMr69Zo9SYsNBRNSJzdRb1qFeEuCdmwa1w',
#     permission_level = GSheetsPermissionLevel.WRITE
# )

# sheet_df = pd.DataFrame.from_records(
#     sheet.read('A:D'),
#     exclude = ['majorDimension', 'range']
# )
# print(sheet_df)

from dotenv import load_dotenv; load_dotenv()
print(os.environ['TEST'])