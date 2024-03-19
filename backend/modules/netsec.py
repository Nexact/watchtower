import feedparser

def get_netsec():
    url = "https://www.reddit.com/r/netsec/.rss"
    feed = feedparser.parse(url)

    if feed.status == 200:
        radiocanada_data = {
            "feedname": "netsec",
            "items": []
        }

        for entry in feed.entries:
            title = entry.title
            href = entry.link

            radiocanada_data['items'].append({'title': title, 'href': href})

        return radiocanada_data
    else:
        print("Failed to retrieve Netsec page.")
        return None