from webbrowser import Chrome
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def DefGoogleUrl(browser):
     browser.get('https://www.google.com/')
     sleep(0.5)

def OpenGoogleWindow(Show=False):
    options = Options()
    if Show == False:
        options.add_argument('--headless')
    options.add_argument('window-size=700,700')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get('https://www.google.com/')
    return browser

def ClickGoogleLink(browser):
    full_html = browser.find_element(By.ID, 'rso')#full result page
    page_first_link = full_html.find_element(By.TAG_NAME, 'h3').click()#first link

def SubmitSearch(browser, keyword='google'):
    sleep(0.5)
    input_search_place = browser.find_element(By.TAG_NAME, 'input')
    input_search_place.send_keys(keyword)
    input_search_place.submit()