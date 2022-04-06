from bs4 import BeautifulSoup
import requests
from pprint import pprint as pp
import csv

URL = "https://www.sulpak.kg/f/smartfoniy"
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

response = requests.get(URL, headers=HEADERS, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('li', class_ = 'tile-container')

phones = []

for item in items:
    phones.append({
        'Название':item.find('h3', class_ = 'title').get_text(strip=True),
        'Отзыв':item.find('div', class_ = 'rating-container r-con').get_text(strip=True),
        'Код товара':item.find('span', class_ = 'code').get_text(strip=True)[12:],
        'Цена':item.find('div', class_ = 'price').get_text(strip=True)[5:]
    })
    
    columns = ['Название','Отзыв','Код товара','Цена']
    
    with open('phones.csv','w') as f:
        writer = csv.DictWriter(f,fieldnames=columns)
        writer.writeheader()
        writer.writerows(phones)
    