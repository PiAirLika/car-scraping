import requests
from bs4 import BeautifulSoup
baseUrl = 'https://occasion.largus.fr/rhone-alpes/'

response = requests.get(baseUrl, verify=False)

if response.ok:
    swupGang = BeautifulSoup(response.text, 'html.parser')
    a = swupGang.find_all('a', {"class": "data-marque"}, {"class": "data-modele"}, {"class": "data-title"}, {"class": "data-marque"})
    for a_ in a:
        ul = a_.find_all('ul', {"class": "list-unstyled"})
        for ul_ in ul:
            lis = ul_.findAll('li')
            for li in lis:
                b = li.find('b')
                if b is not None:
                    try:
                        print(baseUrl + b['href'])
                    except:
                        pass
