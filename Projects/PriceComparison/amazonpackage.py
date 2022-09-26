from webbrowser import Chrome
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

PRODUCT ='rtx'
Amz_List = []

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

def SubmitSearch(browser):
    input_search_place = browser.find_element(By.TAG_NAME, 'input')
    input_search_place.send_keys('amazon')
    input_search_place.submit()
    
def FindAmzProducts(browser):
    input_search_amz = browser.find_element(By.ID, 'twotabsearchtextbox')
    input_search_amz.send_keys(PRODUCT)
    input_search_amz.submit()
    
def WriteAmzProducts(browser):
    main = 'https://www.amazon.com.br'  
    url = f'https://www.amazon.com.br/s?k={PRODUCT}'
    response = requests.get(url)
    
    while not response.ok:
        browser.refresh()
        response = requests.get(url)
        print(response)
        sleep(1)

    content = response.content
    site = BeautifulSoup(content, 'html.parser')

    AllProducts = site.findAll('div', attrs={'class':'a-section a-spacing-base'})
    for product in AllProducts:
        prod_name = product.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        prod_price = product.find('span', attrs={'class':'a-offscreen'})
        prod_link = product.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        click_link = main + prod_link.attrs['href']
        
        if prod_name and prod_price and prod_link != None:
            Amz_List.append([prod_name.text, prod_price.text, click_link])
    
    df_prod = pd.DataFrame(Amz_List, columns=['Product Name', 'Product Price', 'Product Link'])
    df_prod.to_excel("AmzProd.xlsx", index=False)
       