from webbrowser import Chrome
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

PRODUCT ='rtx'#Will be defined dynamically by user.

def SearchAmzProduct(browser): #insert product name in searchbar.
    sleep(1)
    input_search_amz = browser.find_element(By.ID, 'twotabsearchtextbox')
    input_search_amz.send_keys(PRODUCT)
    input_search_amz.submit()
    
    
def GetResponse(browser):
    response = requests.get(browser.current_url)
    count = 1
    while not response.ok:#waits for <Response [200]>
        response = requests.get(browser.current_url)
        count += 1
        print(response)
        if count > 50:
            print(f"Wasn't possible to connect with amazon server, error {response} ")
            exit(0)
    return response


def GetMainHTML(browser):
    response =  GetResponse(browser) #stablish a stable connection with server.
    content = response.content #Extract page html.
    site_html = BeautifulSoup(content, 'html.parser')
    return site_html 


def NextPage(browser):
    but = browser.find_elements(By.TAG_NAME, 'svg')
    but[-1].click()
    

def GetAmzProducts(browser): #write product details in a list.
    Amz_List = []
    main = 'https://www.amazon.com.br'
    
    site_html = GetMainHTML(browser)
    last_page = site_html.find('span', attrs={'class':'s-pagination-item s-pagination-disabled'})
    last_page = int(last_page.text)#number of pages.
    
    for page in range(0, last_page):
        site_html = GetMainHTML(browser)
        
        AllProducts = site_html.findAll('div', attrs={'class':'a-section a-spacing-base'})
        for product in AllProducts:#Get info of all products in page.
            prod_name = product.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
            prod_price = product.find('span', attrs={'class':'a-offscreen'})
            prod_link = product.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
            click_link = main + prod_link.attrs['href']    
            if prod_name and prod_price and prod_link != None:
                Amz_List.append([prod_name.text, prod_price.text, click_link])
                
        NextPage(browser)
        sleep(3)
        
    return Amz_List
    

def TableToExcel(Amz_list): #format the list to data frame and convert it to excel.
    df_prod = pd.DataFrame(Amz_list, columns=['Product Name', 'Product Price', 'Product Link'])
    df_prod.to_excel("ExcelFiles/AmzProd.xlsx", index=False)