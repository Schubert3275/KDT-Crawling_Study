"""
Wikipedia 페이지 가져오기
"""
# Kevin Bacon 위키피디아 URL
#  http://en.wikipedia.org/wiki/Kevin_Bacon
# 임의의 위키 페이지에서 모든 링크 목록 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
