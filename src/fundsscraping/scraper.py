"""Module that provides functions for web scrapping."""

from io import StringIO
from time import sleep

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.parsers import Parser
from .realstate.realstate_fund import RealStateFund
from .sources.status_invest import StatusInvest


def __request_html(page_url: str) -> Firefox:
    options = FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--private')

    browser = Firefox(options=options)
    browser.get(page_url)

    # Roll to the end (load all elements)
    browser.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
    sleep(5)

    return browser


def get_real_state_fund(fund_code: str) -> RealStateFund:
    """Scrap funds data from statusinvest based on fund's name."""

    real_state_fund = RealStateFund(
        name=None,
        metrics={},
        allocation_by_segments={}
    )

    try:
        fund_url = f'{StatusInvest.DOMAIN}{StatusInvest.ROUTE_REAL_STATE}/{fund_code.lower()}'
        browser = __request_html(fund_url)

        # DEBUG
        # html = browser.find_element(
        #     By.TAG_NAME, 'body').get_attribute('innerHTML')
        # print('\n\nHTML HEREEEEEE\n\n')
        # print(html)
        # print('\n\n')

        # General data
        real_state_fund.name = browser.find_element(
            By.TAG_NAME, 'h1').text.split(' ')[0]
        info_divs = browser.find_elements(By.CSS_SELECTOR, 'div.info')

        real_state_fund.metrics['current_value'] = Parser.string_to_float(
            info_divs[0].find_element(By.CSS_SELECTOR, 'strong.value').text)

        real_state_fund.metrics['dividend_yield'] = Parser.string_to_float(
            info_divs[3].find_element(By.CSS_SELECTOR, 'strong.value').text)

        real_state_fund.metrics['asset_value'] = Parser.string_to_float(
            info_divs[5].find_element(By.CSS_SELECTOR, 'strong.value').text)

        real_state_fund.metrics['p_vp'] = Parser.string_to_float(info_divs[6].find_element(
            By.CSS_SELECTOR, 'strong.value').text)

        real_state_fund.metrics['last_income'] = Parser.string_to_float(
            info_divs[15].find_element(By.CSS_SELECTOR, 'strong.value').text)

        # Portfolio ----> Create logic to iterate nav pages, and tabs (if needed)
        try:
            net_equity_container = browser.find_elements(
                By.CLASS_NAME, 'data-percentual-patrimonio')[0]

            real_state_fund.metrics['net_equity'] = Parser.string_to_float(
                net_equity_container.find_elements(By.CLASS_NAME, 'value')[-1].text)

            portfolio_table = browser.find_element(
                By.ID, 'portfolio-FIIRelateds-list').find_elements(By.TAG_NAME, 'table')[-1]

            table_content = pd.read_html(
                StringIO(f'<table>{portfolio_table.get_attribute("innerHTML")}</table>'))

            df = table_content[0][['SEGMENTO', 'INVESTIDO']].copy()
            df.loc[:, 'INVESTIDO'] = df['INVESTIDO'].apply(
                Parser.string_to_float)
            df = df.groupby('SEGMENTO').sum().reset_index()

            for _, row in df.iterrows():
                segment = row['SEGMENTO']
                invested_percentage = (
                    row['INVESTIDO'] / real_state_fund.metrics['net_equity']) * 100

                real_state_fund.allocation_by_segments[segment] = invested_percentage
        except (NoSuchElementException, IndexError) as error:
            print(error)

    except error:
        print(error)

    finally:
        browser.quit()

    return real_state_fund
