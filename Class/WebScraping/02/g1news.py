import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')#stablish connection
content = response.content #get the html
site = BeautifulSoup(content, 'html.parser')#organize the html

#HTML news
news = site.find('div', attrs={'class': 'feed-post-body'})

#News title
title = news.find('a', attrs={'class': 'feed-post-link'})

#News link
link = title.attrs['href']
print(news.prettify())
print(f'Title -> {title.text}')
print(f"Link -> {link}")