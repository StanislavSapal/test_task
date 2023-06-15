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

# for url in travel_urls:
#     print(url)

# /travel/hotels/2023/04/02/qasr-al-sarab-desert-resort-exudes-tranquillity-and-old-world-charm-hotel-insider/
# /travel/2023/05/18/the-best-50-beaches-in-the-world-australia-seychelles-and-philippines-take-top-spots/
# /business/aviation/2023/06/14/airbus-raises-20-year-forecast-for-new-jet-deliveries/
# /travel/2023/06/12/riyadh-air-takes-flight-over-saudi-arabias-capital/
# /travel/2023/05/23/saudi-arabia-to-open-azulik-alula-an-otherworldly-eco-resort-in-the-desert/
# /travel/2023/03/10/nine-things-to-see-and-do-in-khor-fakkan-from-waterfalls-and-beaches-to-mountainous-hikes/
# /travel/2023/06/13/emirates-premium-economy-a380-india-flights/
# /travel/2023/04/15/towering-rixos-marina-abu-dhabi-offers-family-fun-and-endless-relaxation-hotel-insider/
# /travel/2023/05/09/designs-revealed-for-dubai-reefs-worlds-largest-ocean-restoration-and-ecotourism-project/
# /travel/2023/04/25/fifty-years-of-project-tiger-and-indias-commitment-to-the-big-cats/
# /travel/2023/05/26/seouls-great-palace-is-opening-to-night-tourists-for-first-time-since-covid-19-pandemic/
# /travel/2023/06/13/summer-holiday-deals-from-cebu-pacifics-dh1-fare-to-etihad-airways-flight-sale/
# /travel/2023/03/02/marriott-resort-palm-jumeirah-is-dubais-newest-family-friendly-getaway-hotel-insider/
# /travel/2023/05/01/uae-travellers-want-sustainable-trips-but-cost-is-a-barrier-survey-finds/
# /travel/2023/05/21/k-pops-enhypen-to-host-travellers-at-zaha-hadid-designed-dongdaemun-plaza-in-seoul/
# /travel/2023/05/31/why-are-flights-so-expensive-right-now-and-how-to-find-cheaper-airfares/
