import requests
from bs4 import BeautifulSoup

def parse_soup(soup):
    try:
        name = soup.find_all("span", {"class": "username"})
        name = name[4].text.strip()
        name = name[1:]
        print(name)
        tweet = soup.find_all("p", {"class": "TweetTextSize--jumbo"})
        tweet = tweet[0].text.strip()
        # print(tweet)
        try:
            retweets = soup.find_all("a", {"class": "request-retweeted-popup"})
            retweets = retweets[0].text.strip()
            retweets = retweets.split(" ")
            retweets = retweets[0]
            retweets = int(retweets.replace(",",""))
        except:
            retweets = 0
            print(retweets)
        try:
            likes = soup.find_all("a", {"class": "request-favorited-popup"})
            likes = likes[0].text.strip()
            likes = likes.split(" ")
            likes = likes[0]
            likes = int(likes.replace(",",""))
        except:
            likes = 0
        # print(likes)
        timestamp = soup.find_all("span", {"class": "metadata"})
        timestamp = timestamp[0].text.strip()
        timestamp = timestamp.split("- ")
        timestamp = timestamp[1]
        try:
            timestamp = timestamp.split("from")
            timestamp = timestamp[0].strip()
        except:
            timestamp = timestamp
        data = ("name is: " + str(name) + " / retweets: " + str(retweets) + " / likes: " + str(likes) + " / timestamp: " + str(timestamp))
        print(data)
        return (data)
        # print(timestamp)
    except:
        pass


def get_page_soup(url, session):
    try:
        response = session.get(url)
        return BeautifulSoup(response.text, "html.parser")
    except:
        print("Couldn't find url: {}".format(url))
        return None

def gen_data(list):
    with requests.Session() as session:
        for link in list:
            soup = get_page_soup(link, session)
            if soup is None: continue
            parsed = parse_soup(soup)

            yield parsed

links = ["https://twitter.com/Aydren/status/994326702284140544",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",
        "https://twitter.com/Aydren/status/994326702284140544",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",
        "https://twitter.com/Aydren/status/994326702284140544",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",]

data = gen_data(links)
for link in data:
    pass
