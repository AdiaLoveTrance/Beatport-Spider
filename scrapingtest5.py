from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import re

downloadDirectory="downloaded"
baseUrl="http://pythonscraping.com"

def getAbsoluteURL(baseUrl,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        url="http://"+source[4:]
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path=absoluteUrl.replace("www.","")
    path=path.replace(baseUrl,"")
    path = re.sub("\?.*", "", path)  # 把问号开头的字符串都替换为空
    path=downloadDirectory+path
    directory=os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html=urlopen("http://simpledesktops.com/")
bsobj=BeautifulSoup(html)
downloadList=bsobj.findAll(src=True)

for download in downloadList:
    fileUrl=getAbsoluteURL(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))