import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument('window-size=500,500')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.get('https://www.google.com/')

input_search_place = browser.find_element(By.TAG_NAME, 'input')
input_search_place.send_keys('amazon')
input_search_place.submit()
sleep(0.5)

full_html = browser.find_element(By.ID, 'rso')#full result page
page_first_link = full_html.find_element(By.TAG_NAME, 'h3').click()#first link

sleep(0.5)

input_search_amz = browser.find_element(By.ID, 'twotabsearchtextbox')
input_search_amz.send_keys('rtx')
input_search_amz.submit()
sleep(10)
