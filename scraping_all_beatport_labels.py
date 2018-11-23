from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time
import requests
# -*- coding: UTF-8 -*-


def GetMoreDerails(url, album_name, session):

    time.sleep(2)
    nurl = "https://www.beatport.com" + url
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
               "Accept": "*/*"}
    html = session.get(nurl, headers=headers)
    bsobj = BeautifulSoup(html.text, "html.parser")
    find_clog = bsobj.findAll("li", {"class" : "interior-release-chart-content-item"})
    li = find_clog[2]
    catalog = li.find("span", {"class" : "value"}).string
    details = bsobj.findAll("div", {"class" : "buk-track-meta-parent"})
    music_info = []
    for dt in details:
        track_title = dt.find("p", {"class" : "buk-track-title"})
        t1 = track_title.find("span", {"class" : "buk-track-primary-title"}).string
        t2 = track_title.find("span", {"class" : "buk-track-remixed"}).string
        try:
            track_name = t1 + '(' + t2 + ')'
        except TypeError:
            track_name = t1
        track_artists = dt.find("p", {"class" : "buk-track-artists"}).get_text().replace('\n', '').replace(' ', '')
        track_remixers = dt.find("p", {"class" : "buk-track-remixers"}).get_text().replace('\n', '').replace(' ', '')
        track_genre = dt.find("p", {"class" : "buk-track-genre"}).get_text().replace('\n', '').replace(' ', '')
        track_bpm = dt.find("p", {"class" : "buk-track-bpm"}).string
        track_key = dt.find("p", {"class" : "buk-track-key"}).string
        track_length = dt.find("p", {"class" : "buk-track-length"}).string
        info = {'Album' : album_name,
                'Name' : track_name,
                'Artists' : track_artists,
                'Remixers' : track_remixers,
                'Genre' : track_genre,
                'Bpm' : track_bpm,
                'Key' : track_key,
                'Length' : track_length,
                'Catalog' : catalog}
        music_info.append(info)

    return music_info


def PrintReleases(urllinks, company_name, session):

    headers = {"User-Agent": "Mozilla/5.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    html = session.get("https://www.beatport.com"+urllinks, headers=headers)
    bsobj=BeautifulSoup(html.text,"html.parser")
    releases=bsobj.findAll("li",{"class":"bucket-item ec-item horz-release"})
    for release in releases:
        str=release["data-ec-d1"]+" - "+release["data-ec-name"]
        details = release.find("div", {"class" : "horz-release-artwork-parent"})
        href = details.find("a")['href']
        info = GetMoreDerails(href, str, session)
        Write2csv(info, company_name)
        fileobject.write(str+"\n")
        print(str)
    try:
        nextpage=bsobj.find("a",{"class":"pag-next"}).attrs['href']
    except AttributeError:
        print("到达最后一页")
    else:
        PrintReleases(nextpage, company_name, session)

def Write2csv(rows, csvname):
    with open(str(csvname) + '.csv', 'a+', encoding='utf-8') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(rows)

if __name__ == "__main__":

    company_name = "Statement"
    url = "/label/statement%21/3175/releases"

    session = requests.Session()
    fileobject = open(str(company_name) + ".txt", "w", encoding='utf-8')
    headers = ['Album', 'Name', 'Artists', 'Remixers', 'Genre', 'Bpm', 'Key', 'Length', 'Catalog']
    with open(str(company_name) + '.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()

    PrintReleases(url, company_name, session)
