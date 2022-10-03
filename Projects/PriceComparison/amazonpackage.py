from webbrowser import Chrome
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

PRODUCT ='rtx'#Will be defined dynamically by user.

def FindAmzProducts(browser): #insert product name in searchbar.
    sleep(1)
    input_search_amz = browser.find_element(By.ID, 'twotabsearchtextbox')
    input_search_amz.send_keys(PRODUCT)
    input_search_amz.submit()
    

def WriteAmzProducts(browser): #write product details in a list.
    Amz_List = []
    main = 'https://www.amazon.com.br'
    response = requests.get(browser.current_url)
    while not response.ok:#waits for <Response [200]>
        response = requests.get(browser.current_url)
        print(response)

    content = response.content #Extract page html.
    site = BeautifulSoup(content, 'html.parser')
    AllProducts = site.findAll('div', attrs={'class':'a-section a-spacing-base'})
    
    for product in AllProducts:#Get info of all products in page.
        prod_name = product.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        prod_price = product.find('span', attrs={'class':'a-offscreen'})
        prod_link = product.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        click_link = main + prod_link.attrs['href']
        
        if prod_name and prod_price and prod_link != None:
            Amz_List.append([prod_name.text, prod_price.text, click_link])
    
    TableToExcel(Amz_List)

def TableToExcel(Amz_list): #format the list to data frame and convert it to excel.
    df_prod = pd.DataFrame(Amz_list, columns=['Product Name', 'Product Price', 'Product Link'])
    df_prod.to_excel("ExcelFiles/AmzProd.xlsx", index=False)