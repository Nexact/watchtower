import feedparser

def get_lapresse():
    url = "https://www.lapresse.ca/manchettes/rss"
    feed = feedparser.parse(url)

    if feed.status == 200:
        lapresse_data = {
            "feedname": "lapresse",
            "items": []
        }
        for entry in feed.entries:
            title = entry.title
            href = entry.link

            lapresse_data["items"].append({'title': title, 'href': href})

        return lapresse_data
    else:
        print("Failed to retrieve Lapresse page.")
        return None