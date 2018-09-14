from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://www.beatport.com/label/silk-music/13068/releases")
bsobj=BeautifulSoup(html,"html.parser")
imageLocation=bsobj.findAll("div",{"class":"horz-release-artwork-parent"}).find("img")["data-src"]
# print(imageLocation)
k=0;
for image in imageLocation:
    k=k+1;
    name="logo"+str(k)+".jpg"
    urlretrieve(image,name)