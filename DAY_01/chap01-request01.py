"""
멜론 웹사이트 접근 #1
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 샘플 코드 1
# urllib.error.HTTPError: HTTP Error 406: Not Acceptable 발생
# - 사람이 아닌 봇으로 인식해서 크롤링을 막음
# - User Agent 정보가 없음

melon_url = 'https://www.melon.com/chart/index.htm'
html = urlopen(melon_url)

soup = BeautifulSoup(html.read(), 'html.parser')
print(soup)
