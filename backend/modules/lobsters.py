import feedparser

def get_lobsters():
    url = "https://lobste.rs/rss"
    feed = feedparser.parse(url)

    if feed.status == 200:
        lobsters_data = {
            "feedname": "lobsters",
            "items": []
        }
        
        for entry in feed.entries:
            title = entry.title
            href = entry.link

            lobsters_data["items"].append({'title': title, 'href': href})

        return lobsters_data
    else:
        print("Failed to retrieve Lobsters page.")
        return None