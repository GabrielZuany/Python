import requests
from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

def DefGoogleUrl(browser):#back to google...
     browser.get('https://www.google.com/')

def OpenGoogleWindow(Show=False):#open the browser window.
    options = Options()
    if Show == False:
        options.add_argument('--headless')
    options.add_argument('window-size=500,500')
    
    try:
        path = getcwd()
        browser = webdriver.Chrome(executable_path=f'{path}/ExtractData_Webscraping/Webdriver/chromedriver.exe',options=options)
    except:
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    browser.get('https://www.google.com/')
    return browser

def ClickGoogleLink(browser): #click in the first link showed after search.
    full_html = browser.find_element(By.ID, 'rso')#full result page
    full_html.find_element(By.TAG_NAME, 'h3').click()#first link

def SubmitSearch(browser, keyword='google'):#insert a keyword in google text bar.
    sleep(1)
    input_search_place = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search_place.send_keys(keyword)
    input_search_place.submit()
    
def GetResponse(browser):
    response = requests.get(browser.current_url)
    count = 1
    while not response.ok:#waits for <Response [200]>
        response = requests.get(browser.current_url)
        count += 1
        print(response)
        if count > 100:#limits the 'time' trying to connect with server.
            print(f"Wasn't possible to connect with amazon server, error {response} ")
            exit(1)
    return response

def GetMainHTML(browser):
    response =  GetResponse(browser) #stablish a stable connection with server.
    content = response.content #Extract page html.
    site_html = BeautifulSoup(content, 'html.parser')
    return site_html 