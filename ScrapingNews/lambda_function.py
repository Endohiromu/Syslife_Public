#SlackのウェブフックURLはGitにあげないこと
#セキュリティーの関係で自動的に無効化される

#モジュール類はAWSのLayerで管理

import json
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import random
import time
import os

def lambda_handler(event, context):
    #Slackに送信する文字列
    text2post = ""
    
    #タイトル、リンクをそれぞれ格納するリスト
    titles = []
    links = []

    #各スクレイピングデータを一時的に保持し、結合時に使用する
    titles2Append = []
    links2Append = []
    #各サイトからのスクレイピングおよび結合
    titles2Append,links2Append = ScrapFromSlad()
    titles += titles2Append
    links += links2Append

    titles2Append,links2Append = ScrapFromAt()
    titles += titles2Append
    links += links2Append

    
    #全結果の中からランダムに指定個数抽出する
    text2post = chooseTopicks(titles,links,5)
    SendToSlack(text2post)
    
    #トリガーのミスで連続してクローリングすることを防ぐため、10秒待機
    time.sleep(1)   
    

def SendToSlack(text):
    hookURL = os.environ["HOOK"]
    requests.post(hookURL, data=json.dumps({
        "text" :text,
    }))
    
def chooseTopicks(titles,links,nums):
    textResult = ""
    indexList = [0,]
    index = 0
    for i in range(nums):
        while index in indexList:
            index = random.randint(0,len(titles)-1)
        indexList.append(index)
        textResult += titles[index] + "\n" + links[index] + "\n"
    return textResult
    
def ScrapFromSlad():
    URL = "https://srad.jp/"
    r = urllib.request.urlopen(URL)
    
    soup = BeautifulSoup(r, "html.parser")
    topDiv = soup.find("div",id="firehoselist")#,id="colBoxTopStories"
    
    titleDiv = topDiv.find_all("h2", class_="story")
    titles = []
    links = []
    
    
    for i,title in enumerate(titleDiv):
        titles.append(title.find("a").text)
        links.append(title.find("a").get("href"))

    return titles,links

def ScrapFromAt():
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
    
    return titles, links

