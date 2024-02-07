"""
requests 모듈 사용 예제
"""
import requests
from bs4 import BeautifulSoup

# url = 'http://www.pythonscraping.com/pages/page1.html'
url = 'http://finance.naver.com'
# url = 'http://www.naver.com'

html = requests.get(url)
print("html.encoding:", html.encoding)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

print()
print("h1.string:", soup.h1.string)
