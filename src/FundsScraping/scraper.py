from io import StringIO
from time import sleep

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.parsers import parse_string_to_float
from FundsScraping.StatusInvest import StatusInvest
from FundsScraping.RealState.RealStateFund import RealStateFund


def __request_html(page_url: str) -> Firefox:
    options = FirefoxOptions()
    options.add_argument('--headless')

    browser = Firefox(options=options)
    browser.get(page_url)

    # Roll to the end (load all elements)
    browser.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
    sleep(5)

    return browser


def get_real_state_fund(fund_code: str) -> (RealStateFund|None):
    name = None
    current_value = None
    dividend_yield = None
    asset_value = None
    p_vp = None
    last_income = None
    net_equity = None
    allocation_by_segments = {}

    try:        
        fund_url = f'{StatusInvest.DOMAIN}{StatusInvest.ROUTE_REAL_STATE}/{fund_code.lower()}'
        browser = __request_html(fund_url)
        
        # DEBUG
        # html = browser.find_element(By.TAG_NAME, 'body').get_attribute('innerHTML')
        # print('\n\nHTML HEREEEEEE\n\n')
        # print(html)
        # print('\n\n')

        # General data
        name = browser.find_element(By.TAG_NAME, 'h1').text.split(' ')[0]
        info_divs = browser.find_elements(By.CSS_SELECTOR, 'div.info')

        current_value = parse_string_to_float(info_divs[0].find_element(By.CSS_SELECTOR, 'strong.value').text)
        dividend_yield = parse_string_to_float(info_divs[3].find_element(By.CSS_SELECTOR, 'strong.value').text)
        asset_value = parse_string_to_float(info_divs[5].find_element(By.CSS_SELECTOR, 'strong.value').text)
        p_vp = parse_string_to_float(info_divs[6].find_element(By.CSS_SELECTOR, 'strong.value').text)
        last_income = parse_string_to_float(info_divs[15].find_element(By.CSS_SELECTOR, 'strong.value').text)

        # Portfolio ----> Create logic to iterate nav pages, and tabs (if needed)
        try:
            net_equity = parse_string_to_float(browser.find_elements(By.CLASS_NAME, 'data-percentual-patrimonio')[0].find_elements(By.CLASS_NAME, 'value')[-1].text)
            portfolio_table = browser.find_element(By.ID, 'portfolio-FIIRelateds-list').find_elements(By.TAG_NAME, 'table')[-1]
            table_content = pd.read_html(StringIO(f'<table>{portfolio_table.get_attribute("innerHTML")}</table>'))        

            df = table_content[0][['SEGMENTO', 'INVESTIDO']].copy()
            df.loc[:, 'INVESTIDO'] = df['INVESTIDO'].apply(parse_string_to_float)
            df = df.groupby('SEGMENTO').sum().reset_index()

            for _, row in df.iterrows():
                segment = row['SEGMENTO']
                invested_percentage = (row['INVESTIDO'] / net_equity) * 100

                allocation_by_segments[segment] = invested_percentage
        except (NoSuchElementException, IndexError) as error:
            print(error)
    except error:
        print(error)
    finally:
        browser.quit()

        return RealStateFund(
            name = name,
            current_value = current_value,
            dividenv_yield = dividend_yield,
            asset_value = asset_value,
            p_vp = p_vp,
            last_income = last_income,
            net_equity = net_equity,
            allocation_by_segments = allocation_by_segments
        )
