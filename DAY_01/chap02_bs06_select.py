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
BeautifulSoup 기초: select_one() 함수
"""
# ■ select_one()
#   ● 첫 번째 일치하는 태그만 리턴: find()와 동일 기능
#   ● <head> 태그 검색
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text', head.text.strip())
print('-' * 100)

#   ● 첫 번째 <h1> 태그 검색
h1 = soup.select_one('h1')
print(h1)
print('-' * 100)

#   ● <h1> 태그의 id 검색: #id
# <h1> 태그의 id가 "footer"인 항목 추출
footer = soup.select_one('h1#footer')
print(footer)
print('-' * 100)

#   ● 클래스 이름 검색: 태그.클래스이름
#     - <a class="internal_link" href="/pages/page1.html">Page1</a> 검색
class_link = soup.select_one('a.internal_link')
print(class_link)

print(class_link.string)
print(class_link['href'])
print('-' * 100)

# ■ 계층적 하위 태그 접근 #1
#   ● (상위태그 > 하위태그) 형식으로 접근: 태그가 단계적으로 존재할 때
# 계층적 접근
link1 = soup.select_one('div#link > a.external_link')
print(link1)
print('-' * 100)

#   ● find() 함수와 비교
link_find = soup.find('div', {'id': 'link'})

external_link = link_find.find('a', {'class': 'external_link'})
print('find external_link:', external_link)
print('-' * 100)

# ■ 계층적 하위 태그 접근 #2: 공백으로 하위 태그 선언
#   ● (상위태그 하위태그) 형식으로 접근: 자손 관계의 하위태그
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)
print('-' * 100)

# ■ select() 함수
#   ● 모든 <h1> 태그 검색
h1_all = soup.select('h1')
print('h1_all', h1_all)
print('-' * 100)

#   ● 모든 url 링크 검색
# html 문서의 모든 <a> 태그의 href 값 추출
url_links = soup.select('a')
for link in url_links:
    print(link['href'])
print('-' * 100)

#   ● <div id="class1"> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')

print(div_urls)
print(div_urls[0]['href'])
print('-' * 100)

#   ● <div id="class1"> 내부의 모든 <a> 태그는 자손관계
#     - 공백으로 구분할 수 있음
div_urls2 = soup.select('div#class1 a')
print(div_urls2)
print('-' * 100)

# ■ 여러 항목 검색하기
#   ● <h1> 태그의 id가 "heading"과 "footer"를 모두 검색
#     - 쉼표(,)로 나열함
# <h1 id="heading">과 <h1 id="footer"> 항목 가져오기
h1 = soup.select('#heading, #footer')
print(h1)
print('-' * 100)

#   ● <a> 태그의 class이름이 "external_link"와 "internal_link" 모두 검색
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)
