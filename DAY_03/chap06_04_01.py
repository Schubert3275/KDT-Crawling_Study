"""
테이블 데이터를 CSV로 저장: html_table_parser 사용 예제 #1
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs = BeautifulSoup(html, "html.parser")

# 두 개의 테이블 중에 첫 번째 테이블 사용: find_all() 사용
# table = bs.find_all('table', {'class': 'wikitable'})[0]
table = bs.find('table', {'class': 'wikitable'})
table_data = parse.make2d(table)  # 2차원 리스트 형태로 변환

# 테이블의 2행을 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])
