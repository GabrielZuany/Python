from webbrowser import Chrome
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

PRODUCT ='rtx'#Will be defined dynamically by user.

def FindMLProd(browser): #insert product name in searchbar.
    sleep(0.3)
    input_search_label = browser.find_element(By.CLASS_NAME, 'nav-search-input')
    input_search_label.send_keys(PRODUCT)
    input_search_label.submit()

def WriteMLProd(browser): #write product details in a list.
    ML_list = []
    
    url = browser.current_url
    response = requests.get(url)
    print(response)
    while not response.ok: #waits for <Response[200]>
        response = requests.get(url)
        print(response)
    
    content = response.content #Extract page html.
    site = BeautifulSoup(content, 'html.parser')    
    box = site.findAll('li', attrs={'class':'ui-search-layout__item'})
    
    for product_box in box: #Get info of all products in page.
        title = product_box.find('div', attrs={'class':'ui-search-item__group ui-search-item__group--title shops__items-group'})
        symbol_tag = product_box.find('span', attrs={'class':'price-tag-symbol'})
        price = product_box.find('span', attrs={'class':'price-tag-fraction'})
        link_html = product_box.find('a', attrs={'class':'ui-search-result__content ui-search-link'})
        click_link = link_html.attrs['href']
        ML_list.append([title.text, symbol_tag.text + price.text, click_link])
        
    TableToExcel(ML_list)
    
def TableToExcel(ML_list):#format the list to data frame and convert it to excel.
    df_products = pd.DataFrame(ML_list, columns=['Product', 'Price', 'Link'])
    df_products.to_excel('ExcelFiles/ML_list.xlsx', index=False)
    