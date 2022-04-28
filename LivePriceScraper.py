import time
import pandas as pd
from helium import *
from bs4 import BeautifulSoup
import json
import os

url = 'https://www.nepalstock.com.np/live-market'


def openfirefox():
    browser = start_firefox(headless = True)
    return browser
    

def scrape(browser, link):
    browser.get(link)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    table = soup.table
    Liveprice = pd.read_html(str(table))
    time.sleep(2)
    Liveprice = pd.DataFrame(Liveprice[0])
    Liveprice = json.loads('{"items":' + Liveprice.to_json(orient='records', date_format='iso') + '}')
    Liveprice = Liveprice['items']
    return Liveprice
    # df=pd.dataframe()
    # return df
browser = openfirefox()
Liveprice = scrape(browser, url)
print(Liveprice)