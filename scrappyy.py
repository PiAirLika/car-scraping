import requests
from bs4 import BeautifulSoup

base_url = "https://www.idealcars.fr/"
uri = '/vente-de-voitures-w1.html'
response = requests.get(base_url + uri)

def process(soup):
    links = []
    divs = soup.findAll('div', {"class": "ann-titre display-block position-relative"})
    for div in divs :
        car_links = div.findAll("h2", class_="normal-padding-bottom")
        for car in car_links :
            car_links = car.findAll('a') 
            for car_link in car_links :
                links.append(base_url + car_link.get('href'))
    for index, link in enumerate(links) :
        print(f"Voiture n° {index + 1}: {link}")

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    process(soup)