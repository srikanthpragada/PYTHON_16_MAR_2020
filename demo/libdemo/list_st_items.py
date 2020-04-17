import requests
from bs4 import BeautifulSoup
from datetime import datetime

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, 'xml')

today = datetime.today()
for tag in bs.find_all('item'):
    title = tag.title.text.strip()[:50]
    pubdate = tag.pubDate.text[5:17]
    try:
        pdate = datetime.strptime(pubdate.strip(),"%d %b %Y")
        days = (today - pdate).days
        if days < 100:
            print(f"{title:60} {days:2} days")
    except Exception as ex:
        pass


