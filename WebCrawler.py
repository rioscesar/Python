import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    for page in range(1, max_pages+1):
        url = "https://www.thenewboston.com/trade/search.php?page=" + str(page)
        source_code = requests.get(url).text
        soup = BeautifulSoup(source_code)
        for link in soup.findAll('a', {'class' : 'item-name'}):
            href = "https://www.thenewboston.com"+link.get('href') #this is the actual link
            title = link.string #gets the name of the link only
            #print(href, title)
            get_single_item_data(href)

def get_single_item_data(item_url):
    source_code = requests.get(item_url).text
    soup = BeautifulSoup(source_code)
    for item_name in soup.findAll('div', {'class' : 'i-name'})
        print(item_name.string)
    for link in soup.finAll('a'):
        href = "https://www.thenewboston.com"+link.get('href')
        print(href)









trade_spider(1)

