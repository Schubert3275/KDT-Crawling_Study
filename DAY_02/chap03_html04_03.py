"""
트리 이동: 형제 다루기 #1
"""
# 형제: next_siblings 속성
#  임의의 행을 선택하고 next_siblings을 선택하면,
#   - 테이블의 다음 행들을 모두 선택 (모든 형제를 선택)
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

"""
트리 이동: 형제 다루기 #2
"""
# next_siblings 속성
for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
print('-' * 100)

# previous_siblings 속성
#  선택된 행 이전의 항목들을 선택
for sibling in soup.find('tr', {'id': 'gift2'}).previous_siblings:
    print(sibling)
print('-' * 100)

"""
트리 이동: 형제 다루기 #3
"""
# next_sibling, previous_sibling
#  태그 하나만 반환
#  문자열 마지막에 whitespace('\n', '\r'등)가 있는 경우
#   - 해당 whitespace를 next_sibling으로 반환
sibling1 = soup.find('tr', {'id': 'gift3'}).next_sibling
print('sibling1:', sibling1)
print(ord(sibling1))
print('-' * 100)

# next_sibling.next_sibling 이용
sibling2 = soup.find('tr', {'id': 'gift3'}).next_sibling.next_sibling
print(sibling2)
print('-' * 100)

"""
트리 이동: 부모 다루기 #1
"""
# parent 사용
style_tag = soup.style
print(style_tag.parent)
print('-' * 100)

"""
트리 이동: 부모 다루기 #2
"""
# .parent 사용
img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)
