from urllib.request import urlopen
from bs4 import BeautifulSoup
# -*- coding: UTF-8 -*-

fileobject=open("Noir Music.txt", "w", encoding='utf-8')

def PrintReleases(urllinks):
    html=urlopen("https://www.beatport.com"+urllinks)
    bsobj=BeautifulSoup(html,"html.parser")
    releases=bsobj.findAll("li",{"class":"bucket-item ec-item horz-release"})
    for release in releases:
        str=release["data-ec-d1"]+" - "+release["data-ec-name"]
        # print(str)
        fileobject.write(str+"\n")
    try:
        nextpage=bsobj.find("a",{"class":"pag-next"}).attrs['href']
    except AttributeError:
        print("到达最后一页")
    else:
        PrintReleases(nextpage)

PrintReleases("/label/noir-music/6239/releases")
