import feedparser

def get(feedname, url):
    feed = feedparser.parse(url)

    if feed.status == 200:
        data = {
            "feedname": feedname,
            "items": []
        }
        for entry in feed.entries:
            title = entry.title
            href = entry.link

            data["items"].append({'title': title, 'href': href})

        return data
    else:
        print("Failed to retrieve rss feed: {}".format(feedname))
        return None