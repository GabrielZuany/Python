from types import NoneType
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from MainPackages.managerbrowser import GetMainHTML
from os import getcwd
import re

def SearchAmzProduct(browser, product): #insert product name in searchbar.
    sleep(1)
    input_search_amz = browser.find_element(By.ID, 'twotabsearchtextbox')
    input_search_amz.send_keys(product)
    input_search_amz.submit()


def NextPage(browser):
    try:
        but = browser.find_elements(By.TAG_NAME, 'svg')
        but[-1].click()
    except:
        print("Doesn't have more pages.")
    

def GetAmzProducts(browser): #write product details in a list.
    Amz_List = []
    main = 'https://www.amazon.com.br'
    site_html = GetMainHTML(browser)
    
    last_page = site_html.find('span', attrs={'class':'s-pagination-item s-pagination-disabled'})
    
    if type(last_page) != NoneType:#1 page only error
        last_page = int(last_page.text)#number of pages.
    else:
        last_page = 1
    
    for page in range(0, last_page):
        site_html = GetMainHTML(browser)
        
        AllProducts = site_html.findAll('div', attrs={'class':'a-section a-spacing-base'})
        for product in AllProducts:#Get info of all products in page.
            prod_name = product.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
            prod_price = product.find('span', attrs={'class':'a-offscreen'})
            prod_link = product.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
            click_link = main + prod_link.attrs['href']    
            if prod_name and prod_price and prod_link != None:
                price = str(prod_price.text[3:-3])
                price = re.sub('[.]', '', price)
                Amz_List.append([prod_name.text, price, click_link])
                
        NextPage(browser)
        sleep(1)
        
    return Amz_List
    

def TableToExcel(Amz_list): #format the list to data frame and convert it to excel.
    path = getcwd()
    df_prod = pd.DataFrame(Amz_list, columns=['Product', 'Price (R$)', 'Link'])
    df_prod.to_excel(f"{path}/DataAnalysis/ExtractedData/AmzProd.xlsx", index=False)