import requests
from bs4 import BeautifulSoup

url = 'https://www.thenationalnews.com/travel/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')


urls_on_page = [url.get('href') for url in soup.find_all('a')]


urls_on_page.remove(None)

travel_urls = set()

for url in urls_on_page:
    if 'travel/2023' in url or 'travel/hotels' in url or 'business/aviation/2023' in url:
        travel_urls.add(url)
