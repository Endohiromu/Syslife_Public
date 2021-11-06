#SlackのウェブフックURLはGitにあげないこと
#セキュリティーの関係で自動的に無効化される

import json
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import random

def lambda_handler(event, context):
    text2post = ""
    
    titles = []
    links = []
    
    scrapFromSlad(titles,links)
    ScrapFromAt(titles,links)

    
    titles2Append,links2Append = self.ScrapFromNHK()
    titles += titles2Append
    links += links2Append
    
    text2post = chooseTopicks(titles,links,10)
    print(text2post)

#def SendToSlack(text):
    #hookURL = ""
    #requests.post(URL, data=json.dumps({
    #    "text" :text,
    #}))
    
def chooseTopicks(titles,links,nums):
    textResult = ""
    for i in range(nums):
        ind = random.randint(0,len(titles)-1)
        textResult += titles[ind] + "\n" + links[ind] + "\n"
    return textResult
    
def scrapFromSlad(titleArgs, linkArgs):
    URL = "https://srad.jp/"
    r = urllib.request.urlopen(URL)
    
    soup = BeautifulSoup(r, "html.parser")
    topDiv = soup.find("div",id="firehoselist")#,id="colBoxTopStories"
    
    titleDiv = topDiv.find_all("h2", class_="story")
    titles = []
    links = []
    
    
    for i,title in enumerate(titleDiv):
        titleArgs.append(title.find("a").text)
        linkArgs.append(title.find("a").get("href"))
    return

def ScrapFromAt(titleArgs, linkArgs):
    URL = "https://atmarkit.itmedia.co.jp/"
    
    r = urllib.request.urlopen(URL)

    soup = BeautifulSoup(r, "html.parser")
    topDiv = soup.find("div", id="NewsInsight")#,id="colBoxTopStories"

    top = topDiv.find("h3")
    news = topDiv.find_all("li")

    titles,links = [],[]


    for i,title in enumerate(news):
        titles.append(title.find("a").text)
        links.append(title.find("a").get("href"))

def ScrapFromNHK():
    URL = "https://www3.nhk.or.jp/news/cat04.html"
    
    r = urllib.request.urlopen(URL)

    soup = BeautifulSoup(r, "html.parser")
    topDiv = soup.find("div", class="content--items")

    top = topDiv.find_all("li")
    
    titles,links = [],[]


    for i,title in enumerate(news):
        titles.append(title.find("a").text)
        links.append(title.find("a").get("href"))
    
    return titles,links
