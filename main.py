import clipboard
import json
import os
import pandas
import localYFinance as yf
import numpy
from selenium import webdriver
import time
from webdriver_manager import chrome

BASE_JSON_FILE = 'data'

yahoo_finance_ticker_attr_names_for_html = [
    # 'actions',  # debug this, it's returning nothing
    # 'calendar',  # debug this, it's returning nothing
    'history',
    # 'dividends',  # debug this, it's returning nothing
    'financials',  # Financials is the "Income Statement" on Yahoo Finance
    'quarterly_financials',
    'balance_sheet',
    'quarterly_balance_sheet',
    'cashflow',
    'quarterly_cashflow',
]

ticker = yf.Ticker('APHA')

def format_float(numpy_float):
    """
    Converts a numpy64 type to a formatted string.

    Ex: Input => numpy64(99999.6577) Output => '99,999.658'

    @param nupmy64 numpy_float: this is a first param
    @return: this is a description of what is returned
    """
    python_float = numpy_float
    if not isinstance(python_float, float):
        python_float = numpy_float.item()  # numpy method to convert to float
    return f'{round(python_float, 3):,}'

for ticker_attr in yahoo_finance_ticker_attr_names_for_html:
    ticker_panda_obj = getattr(ticker, ticker_attr)

    ticker_type = str(type(ticker_panda_obj))
    # Some of the ticker return values are methods themselves, this is hacky and gross but.. w/e
    if ticker_type == "<class 'method'>":
        ticker_panda_obj = ticker_panda_obj()
    elif ticker_type == "<class 'pandas.core.series.Series'>":
        ticker_panda_obj = pandas.DataFrame(ticker_panda_obj)
    file = open('{}.html'.format(ticker_attr), 'w+')
    file.write(ticker_panda_obj.to_html(
        float_format=format_float
    ))

    # Hacky side effect behavior, makes sure we close all the files before program end
    file.close()

json_file = open(BASE_JSON_FILE, 'w+')
json_file.write(str(json.dumps(ticker.info, indent=4)))

clipboard.copy(os.path.abspath(BASE_JSON_FILE))

driver = webdriver.Chrome(chrome.ChromeDriverManager().install())
driver.get(os.path.abspath('{}.html'.format(yahoo_finance_ticker_attr_names_for_html[0])))
driver.refresh();
# Skip first since that was opened in the initial browser open
# From here on out, out new tabs with hacky inline Javascript in a python file ;)
for ticker_attr in yahoo_finance_ticker_attr_names_for_html[1:]:
    # TODO: Add refresh script fire here to load page
    driver.execute_script("window.open('{}.html');".format(ticker_attr))
    driver.refresh();

print('Done... son!')
