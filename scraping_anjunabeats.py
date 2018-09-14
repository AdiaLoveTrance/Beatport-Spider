from urllib.request import urlopen
from bs4 import BeautifulSoup
# -*- coding: UTF-8 -*-

pages=[]
fileobject=open("BlackHole Recordings.txt","a",encoding='utf-8')
def Getlinks(link):
    global pages
    html = urlopen("https://www.beatport.com" + link)
    bsobj = BeautifulSoup(html, "html.parser")
    for links in bsobj.findAll("a",{"class":"pag-number"}):
        if 'href' in links.attrs:
            if links.attrs['href'] not in pages:
                newpage=links.attrs['href']
                pages.append(newpage)
                # print(newpage)

def PrintReleases(urllinks):
    html=urlopen("https://www.beatport.com"+urllinks)
    bsobj=BeautifulSoup(html,"html.parser")
    releases=bsobj.findAll("li",{"class":"bucket-item ec-item horz-release"})
    for release in releases:
        str=release["data-ec-d1"]+" ———"+release["data-ec-name"]
        # print(str)
        fileobject.write(str+"\n")

PrintReleases("/label/black-hole-recordings/72/releases?page=1")
Getlinks("/label/black-hole-recordings/72/releases?page=1")
for link in pages:
    PrintReleases(link)