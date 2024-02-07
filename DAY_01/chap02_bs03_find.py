# Python 소스 코드 내부에 HTML 문서를 문자열로 저장
html_example = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
"""

"""
BeautifulSoup 기초: find() 함수
"""
# ■ find() 함수
#   ● 해당 조건에 맞는 맨 처음 경과를 추출
#   ● 이름, 속성, 속성값을 이용하여 원하는 태그를 찾을 수 있음
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_example, 'html.parser')
print(soup.find('div'))
print('-' * 100)

#   ● 여러 <div> 태그 중 특정 속성을 가지는 항목 추출
#     - 딕셔너리 형태로 입력 (id속성의 값이 'text_id2'인 항목 검색)
print(soup.find('div', {'id': 'text_id2'}))
print('-' * 100)

#   ● .string, .text(deprecated) 또는 get_text()
#     - 추출된 요소에서 텍스트만 가져옴
div_text = soup.find('div', {'id': 'text_id2'})
print(div_text.text)
print('-' * 100)

print(div_text.string)  # None 리턴

#   ● <a> 태그 및 <a> 태그의 herf 속성 추출
#   ● <a> 태그 중 class 속성값이 "internal_link"인 정보 추출
href_link = soup.find('a', {'class': 'internal_link'})  # 딕셔너리 형태
href_link = soup.find('a', class_='internal_link')  # class_사용: class는 파이썬 예약어

print(href_link)              # <a class="internal_link", ...>
print(href_link['href'])      # <a> 태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href'))  # ['href']와 동일 기능
print(href_link.text)         # <a> Page1 </a> 태그 내부의 텍스트(Page1) 추출
print('-' * 100)

#   ● <a> 태그 내부의 모든 속성 가져오기: attrs
print('href_link.attrs:', href_link.attrs)  # <a> 태그 내부의 모든 속성 출력
print('class 속성값:', href_link['class'])  # class 속성의 value 출력

print('values():', href_link.attrs.values())  # 모든 속성들의 값 출력

values = list(href_link.attrs.values())  # dictionary 값들을 리스트로 변경
print(f'values[0]: {values[0]}, values[1]: {values[1]}')
print('-' * 100)

#   ● href 속성의 값이 'www.google.com'인 항목 검색
href_value = soup.find(attrs={'href': 'www.google.com'})
href_value = soup.find('a', attrs={'href': 'www.google.com'})

print('href_value:', href_value)
print(href_value['href'])
print(href_value.string)
print('-' * 100)

#   ● span 태그의 속성 가져오기
span_tag = soup.find('span')

print('span_tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.string)
print('-' * 100)

#   ● class 속성
#     - class 속성은 여러 개의 값을 가질 수 있음 (multi-valued attribute)
#     - 따라서 list 형태로 리턴함
print('class 속성값:', href_link['class'])
