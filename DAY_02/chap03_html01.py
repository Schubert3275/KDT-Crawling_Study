"""
CSS 속성을 이용한 검색
"""
# ■ 속성(attrs) 사용
#  ● find() 함수에 이름, 속성, 속성값을 이용하여 원하는 태그를 검색
#   - 맨 처음 검색 결과만 리턴
from bs4 import BeautifulSoup

html_text = '<span class="red">Heavens! what a virulent attack!</span>'
soup = BeautifulSoup(html_text, 'html.parser')

object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs:', object_tag.attrs)
print('value:', object_tag.attrs['class'])
print('text:', object_tag.get_text())
