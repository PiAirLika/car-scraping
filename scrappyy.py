import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

base_url = "https://www.idealcars.fr/vente-de-voitures-w1.html"

response = requests.get(base_url, headers=headers)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')

    car_links = soup.find_all("a", class_="cta-1")
    for link in car_links:
        href = link.get("href")
        print(f"Endpoint: {href}")
else:
    print("Impossible d'avoir une réponse de", base_url)