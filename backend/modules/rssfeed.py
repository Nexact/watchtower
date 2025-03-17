import feedparser

def get(feedname, url):
    feedparser.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    feed = feedparser.parse(url)

    print("Getting {} ...".format(url))
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
        print("Failed to retrieve rss feed: {}, error code {}".format(feedname, feed.status))
        return None