import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

from Car import Car

base_url = "https://www.idealcars.fr/"
uri = "vente-de-voitures-w"
nbPages = 11


def swoup(url):
    # Récupération du contenu de la page à l'URL spécifiée
    response = requests.get(url)
    # Vérification que la réponse est valide et création de l'objet BeautifulSoup correspondant
    return BeautifulSoup(response.text, 'lxml') if response.ok else print("Erreur response")


def get_url(page_number):
    # Création de l'URL correspondant à la page spécifiée
    return f"{base_url}{uri}{page_number}.html"


links = []
carList = []

# Extraction des données
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
    # Récupération des informations de la carte de voiture
    link = get_link(car_card)
    name = get_name(car_card)
    brand = get_brand(car_card)
    year = get_year(car_card)
    price = get_price(car_card)
    km = get_km(car_card)
    fuel = get_fuel(car_card)

    # Création d'un objet Car avec les informations extraites
    return Car(link, brand, name, price, fuel, km, year)


def format_car(car_array):
    # Initialisation d'une liste vide pour stocker les données de chaque voiture sous forme de dictionnaire
    car_data = []
    # Pour chaque voiture dans le tableau de voitures, on vérifie si la voiture existe (non nulle)
    for car in car_array:
        if car:
            # Création d'un dictionnaire avec les informations de la voiture
            car_dict = {
                'url': car.get_url(),
                'marque': car.get_brand(),
                'nom': car.get_name(),
                'prix': car.get_price(),
                'carburant': car.get_fuel(),
                'km': car.get_km(),
                'annee': car.get_year()
            }
            # Ajout du dictionnaire de données de la voiture à la liste des données de voiture
            car_data.append(car_dict)

    # Retourne la liste de toutes les données de voiture sous forme de dictionnaires
    return car_data

for page in range(1, nbPages + 1):
    soup = swoup(get_url(page))
    # Récupère toutes les divs correspondant aux annonces de voitures
    car_cards = soup.findAll('div', class_="big-margin-bottom display-flex flex-direction-column cursor-pointer")
    # Récupère les informations de la voiture et les ajoute à la liste pour chaque divs
    for car_card in car_cards:
        carList.append(get_car_info(car_card))

    # carList est une liste d'objets Car
    # On va convertir la liste d'objet en liste de dictionnaire
    list = format_car(carList)
    df = pd.DataFrame(list)
    df.to_csv("car.csv", index=False)
