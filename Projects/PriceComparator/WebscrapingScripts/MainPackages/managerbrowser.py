from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from os import getcwd
import requests


def DefGoogleUrl(browser):
    """
    Redirect the browser to google.com

    Args:
        browser (webdriver): chromedriver with current url (in this case, None).
    """
    browser.get('https://www.google.com/')
    

def OpenGoogleWindow(Show=False):
    """
    Open the browser window.
    
    Args:
        Show (bool, optional): Shows or not the window while webscraping occurs. Defaults to False.

    Returns:
        browser (webdriver): chromedriver with current url (google.com).
    """
    options = Options()
    if Show == False:
        options.add_argument('--headless')
    options.add_argument('window-size=700,700')
    
    #Try to start the webdriver with chromedriver.exe in /Webdriver/. If it fails, make a temporary install.
    try:
        path = getcwd()
        browser = webdriver.Chrome(executable_path=f'{path}/ExtractData_Webscraping/Webdriver/chromedriver.exe',options=options)
    except:
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    browser.get('https://www.google.com/')
    return browser


def ClickGoogleLink(browser):
    """
    Clicks on first link found.

    Args:
        browser (webdriver): browser(chromedriver), with current url.
    """
    full_html = browser.find_element(By.ID, 'rso') # full html page.
    full_html.find_element(By.TAG_NAME, 'h3').click() # first link.


def SubmitSearch(browser, keyword='google'):
    """
    Insert a keyword in google text bar.

    Args:
        browser (webdriver): chromedriver.
        keyword (str, optional): the store to search a product. Defaults to 'google'.
    """
    sleep(1)
    input_search_place = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search_place.send_keys(keyword)
    input_search_place.submit()
    
      
def GetResponse(browser):
    """
    Try to get a stable response with server.
    
    Args:
        browser (webdriver): chromedriver.

    Returns:
        [<Response>]: the response 200, or finish the program.
    """
    response = requests.get(browser.current_url)
    count = 1
    
    while not response.ok:#waits for <Response [200]>
        response = requests.get(browser.current_url)
        count += 1
        print(response)
        if count > 100:#limits the attempts trying to connect with server.
            print(f"Wasn't possible to connect with amazon server, error {response} ")
            exit(1)
    return response


def GetMainHTML(browser):
    """
    Get the page html from response.content.

    Args:
        browser (webdriver): chromedriver.

    Returns:
        HTML: Parsed HTML by BeautifulSoup.
    """
    response =  GetResponse(browser) #stablish a stable connection with server.
    content = response.content #Extract page html.
    site_html = BeautifulSoup(content, 'html.parser')
    return site_html 


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