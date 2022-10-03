from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def DefGoogleUrl(browser):#back to google...
     browser.get('https://www.google.com/')

def OpenGoogleWindow(Show=False):#open the browser window.
    options = Options()
    if Show == False:
        options.add_argument('--headless')
    options.add_argument('window-size=700,700')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get('https://www.google.com/')
    return browser

def ClickGoogleLink(browser): #click in the first link showed after search.
    full_html = browser.find_element(By.ID, 'rso')#full result page
    page_first_link = full_html.find_element(By.TAG_NAME, 'h3').click()#first link

def SubmitSearch(browser, keyword='google'):#insert a keyword in google text bar.
    sleep(1)
    input_search_place = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search_place.send_keys(keyword)
    input_search_place.submit()