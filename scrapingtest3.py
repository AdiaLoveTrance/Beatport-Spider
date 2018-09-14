from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getlinks(pageurl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageurl)
    bsobj=BeautifulSoup(html,"html.parser")
    try:
        print(bsobj.h1.get_text())
        print(bsobj.find(id="mw-content-text").findAll("p")[0])
        print(bsobj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")

    for link in bsobj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage=link.attrs['href']
                print("-----------------\n"+newpage)
                pages.add(newpage)
                getlinks(newpage)

getlinks("")