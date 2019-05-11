import urllib3
from bs4 import BeautifulSoup

data_page = 'https://hearthstone-decks.net/weekly-reports/'
req = urllib3.PoolManager()
page = req.request('GET', data_page)
soup = BeautifulSoup(page.data, 'html.parser')

link = soup.find('a', class_="blog-title")
print(link.get('href'))





