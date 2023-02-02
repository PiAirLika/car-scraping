import requests
from bs4 import BeautifulSoup

base_url = "https://www.idealcars.fr/"
uri = '/vente-de-voitures-w1.html'
response = requests.get(base_url + uri)

def process(soup):
    div = soup.find('div', {"class": "ann-titre display-block position-relative"})
    car_links = div.find_all("h2", class_="normal-padding-bottom")
    for car in car_links :
        links = car.find_all('a') 
    for link in links :
        href = link.get('href')
        car_page = requests.get(base_url + href)
        if car_page.ok:
            car_soup = BeautifulSoup(car_page.text, 'html.parser')
            brand = car_soup.find('strong', {'class': 'marque'})
            price = car_soup.find('strong', {'class': 'prix'})
            print(f"Lien: {href} - Marque: {brand} - Prix: {price}")

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    process(soup)
else:
    print("Impossible d'avoir une réponse de", base_url + uri)