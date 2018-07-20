import aiohttp
import asyncio
import async_timeout
from bs4 import BeautifulSoup
from collections import Counter
import re
from urllib.parse import urlparse
import time

content_area_class = 'entry-content'

async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def soup_d(html, display_result=False):
    soup = BeautifulSoup(html, 'html.parser')
    if display_result:
        print(soup.prettify())
    return soup

async def extract_text(html):
    soup = await soup_d(html)
    content_area = soup.find("div", {"class": content_area_class})
    text = content_area.text
    return text


async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        text = await extract_text(html)
        string = await process_string(text)
        sub_words = string.split()
        words += sub_words
        print(time.time() - start_, "seconds")
        word_freq = Counter(words)
        print("Entire request took", time.time()-start_time, "seconds")
        print(word_freq.most_common(10))



loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main('http://tim.blog'))
except:
    pass
