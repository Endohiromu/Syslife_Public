import urllib.request, urllib.error
from bs4 import BeautifulSoup

URL = "https://srad.jp/"
r = urllib.request.urlopen(URL)

soup = BeautifulSoup(r, "html.parser")

print(URL)

print(soup.select_one("#title-15467057 > a").text)