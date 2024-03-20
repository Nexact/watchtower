import feedparser

def get_rss(feedname, url):
    feed = feedparser.parse(url)

    if feed.status == 200:
        lapresse_data = {
            "feedname": feedname,
            "items": []
        }
        for entry in feed.entries:
            title = entry.title
            href = entry.link

            lapresse_data["items"].append({'title': title, 'href': href})

        return lapresse_data
    else:
        print("Failed to retrieve rss feed.")
        return None