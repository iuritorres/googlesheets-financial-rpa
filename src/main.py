import pandas as pd
from joblib import Parallel, delayed

from GoogleSheet import GoogleSheet
from GSheetsPermissionLevel import GSheetsPermissionLevel
from FundsScraping.scraper import get_real_state_fund

# Move to a Google Workspace module
# -- Google Sheets
# sheet = GoogleSheet(
#     spreadsheet_id = '16tfSBgIJusMr69Zo9SYsNBRNSJzdRb1qFeEuCdmwa1w',
#     permission_level = GSheetsPermissionLevel.WRITE
# )

# sheet_df = pd.DataFrame.from_records(
#     sheet.read('A:D'),
#     exclude = ['majorDimension', 'range']
# )

# print(sheet_df)


# Web Scraping
# real_state_funds = ['XPCI11', 'KNCR11', 'PVBI11', 'LVBI11']
real_state_funds = ['XPCI11']

def get_fund_data(fund_name: str) -> dict:
    return {
        fund_name: {
            'object': get_real_state_fund(fund_name),
            'amount_invested': 1000
        }
    }

result = Parallel(n_jobs=-1)(delayed(get_fund_data)(fund_name) for fund_name in real_state_funds)

real_state_portfolio = {
    fund_name: {
        'object': fund_data['object'],
        'amount_invested': fund_data['amount_invested']
    }
    for fund_dict in result
    for fund_name, fund_data in fund_dict.items()
}

[real_state_portfolio.get(fund).get('object').show_data() for fund in real_state_portfolio.keys()]

# real_state_portfolio = {
#     xpci: 1668.77,
#     kncr: 807.44,
#     pvbi: 522.70,
#     lvbi: 117.07,
# }
