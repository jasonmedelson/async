import asyncio
import aiohttp
import asyncpg
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
        return (data)
        # print(timestamp)
    except:
        pass


async def get_page_soup_async(url, session, sem):
    try:
        async with sem:
            async with session.get(url) as resp:
                response = await resp.text()
        return BeautifulSoup(response, "html.parser")
    except:
        print("Couldn't find url: {}".format(url))
        return None

async def gen_data_async(link):
    async with aiohttp.ClientSession() as session:
        sem = asyncio.Semaphore(1000)
        soup = await get_page_soup_async(link,session,sem)
        # if soup is None: continue
        parsed = parse_soup(soup)
        return parsed

links = ["https://twitter.com/Aydren/status/994326702284140544",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",
        "https://twitter.com/GrantLiffmann/status/1018926952781004802",
        "https://twitter.com/BigWos/status/1018925261885079552",
        "https://twitter.com/Mariannoo/status/1018924799874289666",
        "https://twitter.com/Ballislife/status/1018919744920080384",
        "https://twitter.com/kpelton/status/1018919394020216833",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",
        "https://twitter.com/Aydren/status/994326702284140544",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",
        "https://twitter.com/GrantLiffmann/status/1018926952781004802",
        "https://twitter.com/BigWos/status/1018925261885079552",
        "https://twitter.com/Mariannoo/status/1018924799874289666",
        "https://twitter.com/Ballislife/status/1018919744920080384",
        "https://twitter.com/kpelton/status/1018919394020216833",
        "https://twitter.com/FemSteph/status/994438286020984832",
        "https://twitter.com/summit1g/status/994352812271198208",
        "https://twitter.com/JaceHall/status/995997936357015552",

        ]

async def main(link):
    data = await gen_data_async(link)
    print(data)


loop = asyncio.get_event_loop()
tasks = [loop.create_task(main(link)) for link in links]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
