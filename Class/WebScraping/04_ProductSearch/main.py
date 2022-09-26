import requests
import pandas as pd
from bs4 import BeautifulSoup

product_list = []

base = 'https://lista.mercadolivre.com.br/'
product = input('Which product do you want to search? -> ')
response = requests.get(base + product)
content = response.content
site = BeautifulSoup(content, 'html.parser')

box = site.findAll('li', attrs={'class':'ui-search-layout__item'})

for product_box in box:
    title = product_box.find('h2', attrs={'class':'ui-search-item__title ui-search-item__group__element shops-custom-secondary-font shops__item-title'})
    symbol_tag = product_box.find('span', attrs={'class':'price-tag-symbol'})
    price = product_box.find('span', attrs={'class':'price-tag-fraction'})
    link_html = product_box.find('a', attrs={'class':'ui-search-result__content ui-search-link'})
    click_link = link_html.attrs['href']
    product_list.append([title.text, symbol_tag.text+price.text, click_link])

df_products = pd.DataFrame(product_list, columns=['Product', 'Price', 'Link'])
df_products.to_excel('products.xlsx', index=False)
