import urllib.request, urllib.error
from bs4 import BeautifulSoup

URL = "https://atmarkit.itmedia.co.jp/"
r = urllib.request.urlopen(URL)

soup = BeautifulSoup(r)
topDiv = soup.find("div", id="NewsInsight")#,id="colBoxTopStories"

top = topDiv.find("h3")
news = topDiv.find_all("li")

titles,links = [],[]

titles.append(top.find("a").text)
links.append(top.find("a").get("href"))

for i,title in enumerate(news):
    titles.append(title.find("a").text)
    links.append(title.find("a").get("href"))

print("サイト")
print(URL)
for i in range(len(titles)):
    print(titles[i])
    print(links[i])
