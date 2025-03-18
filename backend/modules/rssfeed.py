import feedparser
import requests
from io import BytesIO

def get(feedname, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}

    print("reading RSS: {}".format(url))
    
    try:
        resp = requests.get(url, headers=headers, timeout=20.0)
    except requests.ReadTimeout:
        print("timeout when reading RSS %s", url)
        return
    content = BytesIO(resp.content)

    feed = feedparser.parse(content)
    if resp.status_code == 200:
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
        print("Failed to retrieve rss feed: {}, error code {}".format(feedname, resp.status_code))
        return None