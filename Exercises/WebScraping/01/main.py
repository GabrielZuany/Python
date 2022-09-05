from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'
response = urlopen(url)#try to open the url

html = response.read()#get site html (messed).

soup = BeautifulSoup(html, 'html.parser')#Organize the html.

print(soup.find('h1', id="hello-world").get_text())
print(soup.find('p', attrs={'class': 'definition'}).get_text())