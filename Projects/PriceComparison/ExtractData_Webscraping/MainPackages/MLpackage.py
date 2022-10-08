from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from MainPackages.managerbrowser import GetMainHTML
from os import getcwd
import re
from types import NoneType

def SearchMLProduct(browser, product): #insert product name in searchbar.
    sleep(0.3)
    input_search_label = browser.find_element(By.CLASS_NAME, 'nav-search-input')
    input_search_label.send_keys(product)
    input_search_label.submit()
    
def AcceptCookies(browser):
    try:
        browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(6) > div.cookie-consent-banner-opt-out > div.cookie-consent-banner-opt-out__actions > button.cookie-consent-banner-opt-out__action.cookie-consent-banner-opt-out__action--primary.cookie-consent-banner-opt-out__action--key-accept").click()
    except:
        print("Doesn't have any cookie requirement")

def NextPage(browser):
    try:
        browser.find_elements(By.CLASS_NAME, 'andes-pagination__arrow-title')[-1].click()
    except:
        print("Doesn't have more pages.")
        
        
def GetMLProducts(browser): #write product details in a list.
    ML_list = []
    AcceptCookies(browser)
    
    last_page = (browser.find_element(By.CLASS_NAME, 'andes-pagination__page-count'))
    
    if type(last_page) != NoneType:#1 page only error
        last_page = last_page.text
        last_page_number = int(last_page[-2]+last_page[-1])
    else:
        last_page_number = 1
    
    for pages in range(0, last_page_number):
        site_html = GetMainHTML(browser)
        box = site_html.findAll('li', attrs={'class':'ui-search-layout__item'}) 
        
        for product_box in box: #Get info of all products in page.
            title = product_box.find('div', attrs={'class':'ui-search-item__group ui-search-item__group--title shops__items-group'})
            price = str(product_box.find('span', attrs={'class':'price-tag-fraction'}).text)
            price = re.sub('[.]', '', price)#to avoid the . floating number error.
            link_html = product_box.find('a', attrs={'class':'ui-search-result__content ui-search-link'})
            click_link = link_html.attrs['href']
            ML_list.append([title.text, price, click_link])
            
        NextPage(browser)
        
    return ML_list 
    
def TableToExcel(ML_list):#format the list to data frame and convert it to excel.
    path = getcwd()
    df_products = pd.DataFrame(ML_list, columns=['Product', 'Price (R$)', 'Link'])
    df_products.to_excel(f'{path}/DataAnalysis/ExtractedData/ML_list.xlsx', index=False)
    