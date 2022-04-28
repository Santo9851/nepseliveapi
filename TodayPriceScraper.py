#For Scraping Today's Price
import pandas as pd
import time
import json
import os
from selenium.webdriver.chrome.options import Options
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.nepalstock.com.np/today-price'




def openfirefox():
    browser = start_firefox(headless = True)
    return browser
    

def scrape(browser, link):
    browser.get(link)
    time.sleep(3)
    items_per_page = browser.find_element(By.XPATH, "//select")
    dropdown = Select(items_per_page)
    dropdown.select_by_visible_text('500')
    click('filter')
    soup = BeautifulSoup(browser.page_source, 'lxml')
    table = soup.table
    todayprice = pd.read_html(str(table))
    #time.sleep(2)
    todayprice = pd.DataFrame(todayprice[0])
    todayprice = json.loads('{"items":' + todayprice.to_json(orient='records', date_format='iso') + '}')
    todayprice = todayprice['items']
    return todayprice


browser = openfirefox()
todayprice = scrape(browser, url)
#todayprice.to_json('todayprice.json')
print(todayprice)