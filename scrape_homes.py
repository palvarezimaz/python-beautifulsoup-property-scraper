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

expanded_links = links + links2 + links3
expanded_images = images + images2 + images3
expanded_addresses = addresses + addresses2 + addresses3
expanded_prices = prices + prices2 + prices3
expanded_features = features + features2 + features3


def create_custom_property_dic(links, images, addresses, prices, features):
    property_dic = []
    for i, item in enumerate(links):
        image = images[i].get('src', None)
        href = item.get('href', None)
        address = addresses[i].getText()
        price = prices[i].getText()
        price = re.sub("[^0-9]", "", price)
        if features[0] != 'Pets':
            beds = features[0].getText()
            baths = features[1].getText()
            car_spots = features[2].getText()
            features = features[3:]

        property_dic.append({'image': image, 'link': href,
                             'address': address, 'price': price, 'beds': beds, 'baths': baths, 'cars': car_spots})
    return property_dic


pprint.pprint(create_custom_property_dic(expanded_links, expanded_images,
              expanded_addresses, expanded_prices, expanded_features))
