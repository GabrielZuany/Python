import requests
from bs4 import BeautifulSoup
import pandas as pd

news_list = []

response = requests.get('https://g1.globo.com/')
content = response.content #get the html
site = BeautifulSoup(content, 'html.parser')#organize the html

#HTML news
Allnews = site.findAll('div', attrs={'class': 'feed-post-body'})

for news in Allnews:
    title = news.find('a', attrs={'class': 'feed-post-link'})
    link = title.attrs['href']
    news_list.append([title.text, link])
      
df_news = pd.DataFrame(news_list, columns=['Title', 'Link'])
df_news.to_excel('news.xlsx', index=False)
