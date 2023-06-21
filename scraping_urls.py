import requests
from bs4 import BeautifulSoup

url = 'https://www.thenationalnews.com/travel/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')



a_tags = soup.find('div', class_='col-sm-xl-12 layout-section wrap-bottom').find_all('a')
a_text = [tag.text for tag in a_tags if tag.text not in ['Travel', '', 'Hotel']]
urls_on_page = [url.get('href') for url in a_tags]

articles_quantity = len(a_text)

urls_on_page.remove(None)

travel_urls = set()

for url in urls_on_page:
    if 'travel/2023' in url or 'travel/hotels' in url or 'business/aviation/2023' in url:
        travel_urls.add(url)
