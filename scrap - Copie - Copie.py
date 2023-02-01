import requests
from bs4 import BeautifulSoup

base_url = "https://www.idealcars.fr/vente-de-voitures-w1.html"

response = requests.get(base_url)

print(response)

