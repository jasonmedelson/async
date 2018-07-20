import shutil
import mechanicalsoup
import bs4
from bs4 import *
from bs4 import BeautifulSoup
import urllib.request as urlreq
import os
import asyncio
#file_location = input("Please enter file location: ")
#os.path.normpath(file_location)

def ParseTwitter(links):
    print("starting link parsing")
    for link in range(len(links)):
        url = links[link]
        try:
            req = urlreq.urlopen(url)
            soup = BeautifulSoup(req)
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
            # print(retweets)
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
            # print(timestamp)
            wbcopy_sheet.write(row, 0, timestamp)
        except:
            pass
    print(str(len(links)+1) + " parsed")

def main():
    links = ["https://twitter.com/Aydren/status/994326702284140544",
            "https://twitter.com/FemSteph/status/994438286020984832",
            "https://twitter.com/summit1g/status/994352812271198208",
            "https://twitter.com/JaceHall/status/995997936357015552",
            "https://twitter.com/Aydren/status/994326702284140544",
            "https://twitter.com/FemSteph/status/994438286020984832",
            "https://twitter.com/summit1g/status/994352812271198208",
            "https://twitter.com/JaceHall/status/995997936357015552"
            "https://twitter.com/Aydren/status/994326702284140544",
            "https://twitter.com/FemSteph/status/994438286020984832",
            "https://twitter.com/summit1g/status/994352812271198208",
            "https://twitter.com/JaceHall/status/995997936357015552"]
    ParseTwitter(links)


if __name__ == "__main__":
    main()
