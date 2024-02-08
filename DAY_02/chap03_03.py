"""
링크간 무작위 이동하기: 소스코드
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

# random.seed(datetime.datetime.now())
random.seed(None)  # Python 3.9 이상

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    body_content = bs.find('div', {'id': 'bodyContent'})
    wikiUrl = body_content.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    return wikiUrl


links = getLinks('/wiki/Kevin_Bacon')
print('links 길이:', len(links))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
