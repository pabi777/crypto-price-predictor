from selenium import webdriver
import pandas as pd
from time import sleep
import csv

url = "https://in.investing.com/crypto/currencies/"
driver = webdriver.Chrome('libs/chromedriver')
driver.get(url)
t = 10


def closepopup(driver):
    try:
        driver.find_element_by_xpath(
            "//i[@class='popupCloseIcon largeBannerCloser']").click()
    except:
        print("no popup")


def scrape_data():
    try:
        sleep(5)
        table = driver.find_element_by_xpath(
            "//table[@class='genTbl openTbl js-all-crypto-table mostActiveStockTbl crossRatesTbl allCryptoTlb wideTbl elpTbl elp15']//tbody")
        headers = ['serial', 'icon', 'Name', 'Symbol',
                   'Price (USD)', 'Market Cap', 'Vol (24H)', 'Total Vol', 'Chg (24H)', 'Chg (7D)']

        with open('data/livedata.csv', 'w') as csvfile:
            wr = csv.writer(csvfile)
            for row in table.find_elements_by_css_selector('tr'):
                wr.writerow(
                    [d.text for d in row.find_elements_by_css_selector('td')])
    except:
        t = sleep(int(input('Enter sleep time: ')))
        closepopup(driver)
        scrape_data
    finally:
        print("looped")
        t = int(input("press 0 To exit.."))
        if t == 0:
            driver.quit()
            exit()
        scrape_data()


scrape_data()
