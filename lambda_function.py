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
    
    text2post = chooseTopicks(titles,links,5)
    print(text2post)

def SendToSlack(text):
    hookURL = "https://hooks.slack.com/services/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"
    requests.post(URL, data=json.dumps({
        "text" :text,
    }))
    
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
    
