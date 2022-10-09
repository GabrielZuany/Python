from MainPackages.managerbrowser import GetMainHTML
from selenium.webdriver.common.by import By
from types import NoneType
from time import sleep
from os import getcwd
import pandas as pd
import re

def SearchAmzProduct(browser, product): #insert product name in searchbar.
    """
    Found Amazon searchbar and submit a product name.

    Args:
        browser (webdriver): chromedriver.
        product (str): product to be searched.
    """
    sleep(0.5)
    input_search_amz = browser.find_element(By.ID, 'twotabsearchtextbox')
    input_search_amz.send_keys(product)
    input_search_amz.submit()


def NextPage(browser):
    """
    Find the next page button.

    Args:
        browser (webdriver): chromedriver.
    """
    try:
        but = browser.find_elements(By.TAG_NAME, 'svg')
        but[-1].click()
    except:
        print("Doesn't have more pages.")
    

def GetAmzProducts(browser):
    """
    Get all products available in site.

    Args:
        browser (webdriver): chromedriver.

    Returns:
        list: list with all extracted data.
    """
    Amz_List = []
    site_html = GetMainHTML(browser)
    
    last_page = site_html.find('span', attrs={'class':'s-pagination-item s-pagination-disabled'})
    if type(last_page) != NoneType: # Avoid error when exists only 1 page.
        last_page = int(last_page.text)
    else:
        last_page = 1
    
    for page in range(0, last_page): # loops until arrive at last page.
        site_html = GetMainHTML(browser)
        AllProducts = site_html.findAll('div', attrs={'class':'a-section a-spacing-base'})
        Amz_List = GetCurrentPageProducts(AllProducts, Amz_List)
        NextPage(browser)
        
    return Amz_List
    
def GetCurrentPageProducts(AllProducts, AMZ_List):
    """
    Get all products in current page.

    Args:
        AllProducts (HTML): HTML with all products in current page.
        ML_list (list): list to append new products.

    Returns:
        list: updated list.
    """
    main = 'https://www.amazon.com.br'
    
    for product in AllProducts: # get all products in current page.
        prod_name = product.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        prod_price = product.find('span', attrs={'class':'a-offscreen'})
        prod_link = product.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        click_link = main + prod_link.attrs['href']  
          
        if prod_name and prod_price and prod_link != None:
            price = str(prod_price.text[3:-3])
            price = str(re.sub('[.]', '', price)) # Avoid the '.' as floating point.
            price = int(re.sub('[,]', '', price))
            AMZ_List.append([prod_name.text, price, click_link])
            
    return AMZ_List

def TableToExcel(Amz_list):
    """
    Format the list to data frame and convert it to excel.

    Args:
        Amz_list (list): list with extracted data..

    Returns:
        Dataframe: dataframe to build separated plots and/or use for another propose.
    """
    path = getcwd()
    df_prod = pd.DataFrame(Amz_list, columns=['Product', 'AMZ Price (R$)', 'Link'])
    df_prod.to_excel(f"{path}/DataAnalysis/AmzProd.xlsx", index=False)
    return df_prod


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