import pandas as pd

# Move to a Google Workspace module
from GoogleSheet import GoogleSheet
from GSheetsPermissionLevel import GSheetsPermissionLevel

# -- Google Sheets
# sheet = GoogleSheet(
#     spreadsheet_id = '16tfSBgIJusMr69Zo9SYsNBRNSJzdRb1qFeEuCdmwa1w',
#     permission_level = GSheetsPermissionLevel.WRITE
# )

# sheet_df = pd.DataFrame.from_records(
#     sheet.read('A:D'),
#     exclude = ['majorDimension', 'range']
# )


# Web Scraping
from FundsScraping.scraper import get_real_state_fund

xpci = get_real_state_fund('XPCI11')
xpci.show_data()

kncr = get_real_state_fund('KNCR11')
kncr.show_data()

pvbi = get_real_state_fund('PVBI11')
pvbi.show_data()

lvbi = get_real_state_fund('LVBI11')
lvbi.show_data()

real_state_portfolio = {
    xpci: 1668.77,
    kncr: 807.44,
    pvbi: 522.70,
    lvbi: 117.07,
}
