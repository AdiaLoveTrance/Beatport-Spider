import requests
from bs4 import BeautifulSoup

seesion=requests.Session()
headers={"User-Agent":"Mozilla/5.0",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
url="http://whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
req=seesion.get(url,headers=headers)
bsobj=BeautifulSoup(req.text)
print(bsobj.find("table",{"class":"table-striped"}).get_text)