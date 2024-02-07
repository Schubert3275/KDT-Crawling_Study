"""
BeautifulSoup 첫 예제
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.daangn.com/hot_articles")
bs = BeautifulSoup(html.read(), "html.parser")

print(bs.h1)
print(bs.h1.string.strip())
