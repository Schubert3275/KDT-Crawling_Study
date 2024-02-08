"""
항목 링크 찾기
"""
# 항목 fldzm(연관 기사 링크)만 가져오기
#  항목 링크의 3가지 특성을 이용
#  정규식: ^(/wiki/)((?!:).)*$
#   - ^: 정규식 시작, $: 정규식 끝
#   - (/wiki/): '/wiki/' 문자열 포함
#   - ((?!:).)*: ':'이 없는 문자열 및 임의의 문자(.)가 0회 이상(*) 반복되는 문자열 검색
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
body_content = bs.find('div', {'id': 'bodyContent'})

pattern = '^(/wiki/)((?!:).)*$'
for link in body_content.find_all('a', href=re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
