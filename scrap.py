import requests 
from bs4 import BeautifulSoup

base_url = 'https://www.notaires.fr/'
uri = '/fr/directory/offices?location=lyon&lat=45.758&lon=4.835&locality=Lyon&postal_code=69001&search_id=IldG7MnHvo-P9UIZtiUMRKz_QaCssEiFAVE1wDvrW9g'
response = requests.get(base_url + uri)

def process(soup):
    article = soup.find('article', {"class": "notary-card notary-card--office-sheet"})
    divs = article.find_all('div', {"class": "text-end"})    
    for div in divs:
        links = div.find_all('a')
        for link in links:
            print(link)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    process(soup)