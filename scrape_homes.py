import requests
from bs4 import BeautifulSoup
import pprint
import re

res = requests.get(
    'https://www.rent.com.au/properties/rosanna+3084?rent_low=any&rent_high=any&surrounding_suburbs=1')
res2 = requests.get(
    'https://www.rent.com.au/properties/rosanna+3084?rent_low=any&rent_high=any&surrounding_suburbs=2')
res3 = requests.get(
    'https://www.rent.com.au/properties/rosanna+3084?rent_low=any&rent_high=any&surrounding_suburbs=3')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
soup3 = BeautifulSoup(res3.text, 'html.parser')

links = soup.select('.asset')
images = soup.select('.asset > img')
addresses = soup.select('.address')
prices = soup.select('.price')
features = soup.select('.feature > .value')

links2 = soup2.select('.asset')
images2 = soup.select('.asset > img')
addresses2 = soup2.select('.address')
prices2 = soup2.select('.price')
features2 = soup2.select('.feature > .value')

links3 = soup3.select('.asset')
images3 = soup.select('.asset > img')
addresses3 = soup3.select('.address')
prices3 = soup3.select('.price')
features3 = soup3.select('.feature > .value')

three_page_links = links + links2 + links3
three_page_images = images + images2 + images3
three_page_addresses = addresses + addresses2 + addresses3
three_page_prices = prices + prices2 + prices3
three_pages_features = features + features2 + features3


def create_custom_hn(links, images, addresses, prices, features):
    hn = []
    for i, item in enumerate(links):
        image = images[i].get('src', None)
        href = item.get('href', None)
        address = addresses[i].getText()
        price = prices[i].getText()
        price = re.sub("[^0-9]", "", price)
        if features[0] != 'Pets':
            beds = features[0].getText()
            baths = features[1].getText()
            cars = features[2].getText()
            features = features[3:]

        hn.append({'image': image, 'link': href,
                  'address': address, 'price': price, 'beds': beds, 'baths': baths, 'cars': cars})
    return hn


pprint.pprint(create_custom_hn(three_page_links, three_page_images,
              three_page_addresses, three_page_prices, three_pages_features))
