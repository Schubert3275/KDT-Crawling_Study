"""
네이버 블로그 검색
"""
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

query = 'ChatGPT'
url = f'https://search.naver.com/search.naver?where=view&sm=tag_jum&query={query}'

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
blog_results = soup.select('a.title_link')
print('검색 결과수:', len(blog_results))

for blog_title in blog_results:
  title = blog_title.text
  link = blog_title['href']
  print(f'{title}, [{link}]')
