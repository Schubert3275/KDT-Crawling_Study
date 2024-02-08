"""
전체 사이트에서 데이터 수집
■ getLinks() 함수 수정
  ● set 사용: 동일한 페이지를 두 번 크롤링하는 것을 방지
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
count = 0
def getLinks(pageUrl):
    global pages, count
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    try:
      print(bs.h1.get_text())  # <h1> 태그 검색
      print(bs.find(id='mw-content-text').find('p').text)
      # print(bs.find('div', attrs={'id': 'mw-content-text'}).find('p').text)
    except ArithmeticError as e:
      print('This page is missing something! Continuing:', e)

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-' * 40)
                count += 1
                print(f'[{count}]: http://en.wikipedia.org{newPage}')
                pages.add(newPage)
                getLinks(newPage)

getLinks('')
