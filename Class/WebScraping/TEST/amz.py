import requests
from bs4 import BeautifulSoup

main = 'https://www.amazon.com.br'
response = 0

response = requests.get('https://www.amazon.com.br/s?k=ps5+console&crid=U2URHRW0C3AN&sprefix=%2Caps%2C198&ref=nb_sb_ss_recent_1_0_recent')

content = response.content
site = BeautifulSoup(content, 'html.parser')

prod_box = site.find('div', attrs={'class':'a-section a-spacing-base'})

prod_name = prod_box.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
prod_price = prod_box.find('span', attrs={'class':'a-offscreen'})
prod_link = prod_box.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
click_link = main + prod_link.attrs['href']

print(prod_name.text)
print(prod_price.text)
print(click_link)