from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getlinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsobj = BeautifulSoup(html, "html.parser")
    return bsobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links=getlinks("/wiki/Anjunabeats")
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getlinks(newArticle)

