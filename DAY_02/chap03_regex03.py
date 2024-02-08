"""
정규 표현식과 BeautifulSoup #2

■ 대소문자 구분없이 특정 단어 검색
    ● '[T|t]{1}he prince'
        - T 또는 t가 1회
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

princeList = bs.find_all(string='the prince')
print('the prince count:', len(princeList))

prince_list = bs.find_all(string=re.compile('[T|t]{1}he prince'))
print('T|the prince count:', len(prince_list))
