from modules import hackernews 
from modules import rssfeed

import json


if __name__ == "__main__":
    data = []

    hackernews_data = hackernews.get_hackernews()

    rss_feed = [
        {"feedname": "lobster", "url":"https://lobste.rs/rss"},
        {"feedname": "netsec", "url":"https://www.reddit.com/r/netsec/.rss"},
        {"feedname": "bleepingcomputer", "url":"https://www.bleepingcomputer.com/feed/"},
        {"feedname": "krebsonsecurity", "url":"https://krebsonsecurity.com/feed/"},
        {"feedname": "slashdot", "url": "http://rss.slashdot.org/Slashdot/slashdot"},
        {"feedname": "ciscotalos", "url": "https://blog.talosintelligence.com/.rss"}
    ]

    # loop rss feeds
    for feed in rss_feed:
        feedname = feed['feedname']
        url = feed['url']

        data.append(rssfeed.get(feedname, url))

    # html feed
    data.append(hackernews_data)

    # prepare json dump 
    

    print(json.dumps(data, indent=4))
    with open("data.json", "w") as outfile:
        outfile.write(json.dumps(data, indent=4))