import urllib.request, urllib.error
from bs4 import BeautifulSoup

URL = "https://www.itmedia.co.jp/news/"
r = urllib.request.urlopen(URL)

soup = BeautifulSoup(r)
topDiv = soup.find("div",id="colBoxTopStories")#,id="colBoxTopStories"

titleDiv = topDiv.find_all("div", class_="colBoxTitle")
titles = []
links = []


for i,title in enumerate(titleDiv):
    titles.append(title.find("a").text)
    links.append(title.find("a").get("href"))
    
print("サイト")
print(URL)
for i in range(len(titles)):
    print(titles[i])
    print(links[i])
