import requests
from bs4 import BeautifulSoup


def get_hackernews():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('span', class_='titleline')

        hackernews_data = {
            "feedname": "hackernews",
            "items": []
        }

        for item in items:
            link = item.find('a')

            title = link.text
            href = link['href']
                
            hackernews_data["items"].append({'title': title, 'href': href})

        return hackernews_data
    else:
        print("Failed to retrieve Hacker News page.")
        return None
    

class HackerNews:
    def __init__(self, nom):
        self.nom = nom

    def afficher_nom(self):
        print("Nom:", self.nom)