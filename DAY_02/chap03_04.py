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
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새로운 페이지 발견
                newPage = link.attrs['href']
                count += 1
                print(f'[{count}]: {newPage}')
                pages.add(newPage)  # 세트에 추가
                getLinks(newPage)

getLinks('')
