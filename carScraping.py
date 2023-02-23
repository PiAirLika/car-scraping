import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

from Car import Car

base_url = "https://www.idealcars.fr/"
uri = "vente-de-voitures-w"
nbPages = 11


def swoup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml') if response.ok else print("Erreur response")


def get_url(page_number):
    return f"{base_url}{uri}{page_number}.html"


links = []
carList = []


def get_link(card):
    return card.find("h2", class_="normal-padding-bottom").find("a")['href'] if car_card.find("h2", class_="normal-padding-bottom").find("a")['href'] else None


def get_name(card):
    return card.find("h2", class_="normal-padding-bottom").find("a")['title'].split('à')[0].strip() if card.find("h2", class_="normal-padding-bottom") else None


def get_brand(card):
    return card.find("div", class_="marque").findAll("span")[2].text.strip() if card.find("div", class_="marque") else None


def get_year(card):
    return card.find("div", class_="annee").findAll("span")[2].text.strip() if card.find("div", class_="annee") else None


def get_price(card):
    return card.find("div", class_="prix").findAll("span")[1].text.strip().replace('.', '').replace('  ', ' ') if card.find("div", class_="prix") else None


def get_km(card):
    return card.find("div", class_="km").findAll("span")[2].text.strip().replace('.', '').replace(' ', '') + " km" if card.find("div", class_="km") else None


def get_fuel(card):
    return card.find("div", class_="carburant").findAll("span")[2].text.strip() if card.find("div", class_="carburant") else None


def get_car_info(car_card):
    link = get_link(car_card)
    name = get_name(car_card)
    brand = get_brand(car_card)
    year = get_year(car_card)
    price = get_price(car_card)
    km = get_km(car_card)
    fuel = get_fuel(car_card)

    return Car(link, brand, name, price, fuel, km, year)


def format_car(car_array):
    car_data = []
    for car in car_array:
        if car:
            car_dict = {
                'url': car.get_url(),
                'marque': car.get_brand(),
                'nom': car.get_name(),
                'prix': car.get_price(),
                'carburant': car.get_fuel(),
                'km': car.get_km(),
                'annee': car.get_year()
            }
            car_data.append(car_dict)

    return car_data


for page in range(1, nbPages + 1):
    soup = swoup(get_url(page))
    car_cards = soup.findAll('div', class_="big-margin-bottom display-flex flex-direction-column cursor-pointer")
    for car_card in car_cards:
        carList.append(get_car_info(car_card))

    list = format_car(carList)
    df = pd.DataFrame(list)
    df.to_csv("car.csv", index=False)
