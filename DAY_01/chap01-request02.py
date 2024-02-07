"""
멜론 웹사이트 접근 #2
"""
# ■ Request 클래스 사용
#   ● User agent 정보 추가: headers = {'User-Agent': 'Mozilla/5.0'}
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

melon_url = 'https://www.melon.com/chart/index.htm'
# HTTP request 패킷 생성: Request()
urlrequest = Request(melon_url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')

print(soup)
