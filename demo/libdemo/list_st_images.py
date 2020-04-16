
import requests
from bs4 import BeautifulSoup


resp = requests.get("http://www.srikanthtechnologies.com/default.aspx")
bs = BeautifulSoup(resp.text,'html.parser')

for t in bs.find_all("a"):
    if 'href' in t.attrs:
        print(t.attrs['href'])
