import urllib.request, urllib.error
from bs4 import BeautifulSoup

URL = "https://srad.jp/"
r = urllib.request.urlopen(URL)

soup = BeautifulSoup(r)
topDiv = soup.find("div",id="firehoselist")#,id="colBoxTopStories"

titleDiv = topDiv.find_all("h2", class_="story")
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
