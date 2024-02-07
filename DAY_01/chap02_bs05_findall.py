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
BeautifulSoup 기초: find_all() 함수
"""
# ■ 모든 div 태그 검색
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_example, 'html.parser')

# 모든 div 태그를 검색 (리스트 형태로 반환)
div_tags = soup.find_all('div')
print('div_tags length:', len(div_tags))

for div in div_tags:
    print('-' * 50)
    print(div)
print('-' * 100)

# ■ 모든 <a> 태그 검색 및 속성 보기
links = soup.find_all('a')

for alink in links:
    print(alink)
    print(f"url:{alink['href']}, text: {alink.string}")
    print()
print('-' * 100)

# ■ 특정 태그 중 여러 속성값을 한 번에 검색
#   ● 여러 <a> 태그에서 2개의 class 속성값 검색: 'external_link', 'internal_link'만 검색
#     - 검색할 속성값을 리스트 형태로 추가
#     - {'class':['external_link', 'internal_link']}
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)
print('-' * 100)

#   ● <p> 태그의 id 값이 'first', 'third'인 항목 검색
p_tags = soup.find_all('p', {'id':['first', 'third']})
for p in p_tags:
    print(p)
print('-' * 100)
