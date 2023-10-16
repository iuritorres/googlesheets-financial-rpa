import os.path

from GoogleSheet import GoogleSheet
from GSheetsPermissionLevel import GSheetsPermissionLevel

def get_local_env_vars() -> None:
    if os.path.exists('.env'):
        with open('.env', 'r') as env_file:
            for line in env_file:
                line.strip()

                if line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'

sheet = GoogleSheet(
    spreadsheet_id = SPREADSHEET_ID,
    permission_level = GSheetsPermissionLevel.WRITE
)

get_local_env_vars()
print(os.environ.get('TESTEE'))
