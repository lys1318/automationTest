import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

webList = soup.find_all("div", attrs={"class":"col_inner"})

for i in webList:
    day = i.h4.get_text()
    if day == "일요 웹툰":
        webtoonName = i.find_all("a",attrs={"class":"title"})
        for j in webtoonName:
            print(j.get_text())