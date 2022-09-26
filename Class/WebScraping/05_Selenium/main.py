from unicodedata import name
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

nav = webdriver.Chrome(ChromeDriverManager().install())

nav.get('https://www.google.com/')


inputG1 = nav.find_element(By.TAG_NAME, 'input')
inputG1.send_keys('UFES')

sleep(3)
print(inputG1)