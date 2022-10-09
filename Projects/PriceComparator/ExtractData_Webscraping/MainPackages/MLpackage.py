from MainPackages.managerbrowser import GetMainHTML
from selenium.webdriver.common.by import By
from types import NoneType
from time import sleep
from os import getcwd
import pandas as pd
import re

def SearchMLProduct(browser, product):
    """
    Found Mercado Livre searchbar and submit a product name.

    Args:
        browser (webdriver): chromedriver.
        product (str): product to be searched.
    """
    sleep(0.5)
    input_search_label = browser.find_element(By.CLASS_NAME, 'nav-search-input')
    input_search_label.send_keys(product)
    input_search_label.submit()
    
    
def AcceptCookies(browser):
    """
    Click in "Accept Cookies" if it exists.

    Args:
        browser (webdriver): chromedriver.
    """
    try:
        browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(6) > div.cookie-consent-banner-opt-out > div.cookie-consent-banner-opt-out__actions > button.cookie-consent-banner-opt-out__action.cookie-consent-banner-opt-out__action--primary.cookie-consent-banner-opt-out__action--key-accept").click()
    except:
        print("Doesn't have any cookie requirement")


def NextPage(browser):
    """
    Find the next page button.

    Args:
        browser (webdriver): chromedriver.
    """
    try:
        browser.find_elements(By.CLASS_NAME, 'andes-pagination__arrow-title')[-1].click()
    except:
        print("Doesn't have more pages.")
        
        
def GetMLProducts(browser): 
    """
    Get all products available in site.

    Args:
        browser (webdriver): chromedriver.

    Returns:
        list: list with all extracted data.
    """
    ML_list = []
    AcceptCookies(browser)
    
    last_page = (browser.find_element(By.CLASS_NAME, 'andes-pagination__page-count'))
    if type(last_page) != NoneType:# Avoid error when exists only 1 page.
        last_page = last_page.text
        last_page_number = int(last_page[-2]+last_page[-1])
    else:
        last_page_number = 1
    
    for pages in range(0, last_page_number): # loops until arrive at last page.
        site_html = GetMainHTML(browser)
        AllProducts = site_html.findAll('li', attrs={'class':'ui-search-layout__item'}) 
        ML_list = GetCurrentPageProducts(AllProducts, ML_list)     
        NextPage(browser)
        
    return ML_list 
    
   
def GetCurrentPageProducts(AllProducts, ML_list):
    """
    Get all products in current page.

    Args:
        AllProducts (HTML): HTML with all products in current page.
        ML_list (list): list to append new products.

    Returns:
        list: updated list.
    """
    for products in AllProducts: # get all products in current page.
        title = products.find('div', attrs={'class':'ui-search-item__group ui-search-item__group--title shops__items-group'})
        price = str(products.find('span', attrs={'class':'price-tag-fraction'}).text)
        price = re.sub('[.]', '', price) # Avoid the '.' as floating point.
        link_html = products.find('a', attrs={'class':'ui-search-result__content ui-search-link'})
        click_link = link_html.attrs['href']
        ML_list.append([title.text, int(price), click_link])
        
    return ML_list    
    
    
def TableToExcel(ML_list):
    """
    Format the list to data frame and convert it to excel.

    Args:
        ML_list (list): list with extracted data..

    Returns:
        Dataframe: dataframe to build separated plots and/or use for another propose.
    """
    path = getcwd()
    df_products = pd.DataFrame(ML_list, columns=['Product', 'ML Price (R$)', 'Link'])
    df_products.to_excel(f'{path}/DataAnalysis/ML_list.xlsx', index=False)
    return df_products
    
    
    """
    Created by: Gabriel Zuany Duarte Vargas.
    Date: 08/10/2022 (Last update).
    Protected by GNU V3.0.
    
    Copyright (C) <2022>  <Gabriel Zuany Duarte Varga>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.   
    """