import feedparser

def get_radiocanada():
    url = "https://ici.radio-canada.ca/rss/4159"
    feed = feedparser.parse(url)

    if feed.status == 200:
        radiocanada_data = {
            "feedname": "radiocanada",
            "items": []
        }

        for entry in feed.entries:
            title = entry.title
            href = entry.link

            radiocanada_data['items'].append({'title': title, 'href': href})

        return radiocanada_data
    else:
        print("Failed to retrieve Radio-Canada page.")
        return None