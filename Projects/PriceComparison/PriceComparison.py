import amazonpackage
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

browser = amazonpackage.OpenGoogleWindow(Show=True)

amazonpackage.SubmitSearch(browser)
amazonpackage.ClickGoogleLink(browser)
amazonpackage.FindAmzProducts(browser)
sleep(1)

amazonpackage.WriteAmzProducts(browser)
browser.find_element(By.CLASS_NAME, 's-pagination-button').click()
sleep(1)

amazonpackage.WriteAmzProducts(browser)
browser.close()