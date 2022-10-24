from unicodedata import name
from bs4 import BeautifulSoup
import requests

search_link = f'https://www.realtor.com/realestateandhomes-detail/21-Keating-St_Chatsworth_GA_30705_M58347-70261?property_id=5834770261&from=ab_mixed_view_card'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

url = requests.get(url=search_link, headers=headers)
soup = BeautifulSoup(url.text, 'html.parser')

div = soup.find(name='div', class_="main-carousel")

for i in div:
    img = i.find(name='img')
    print(img)