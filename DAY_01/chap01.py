"""
웹 페이지 가져오기
"""
# ■ urllib.request.urlopen(url)
#   ● 해당 url에서 HTML파일이나 이미지 파일, 기타 파일을 가져오는 함수
#   ● 리턴값: HTTPResponse 객체
# ■ HTTPResponse.read()
#   ● HTML 콘텐츠를 읽음 (리턴값: bytes 형태)

from urllib.request import urlopen

html = urlopen('http://www.daangn.com/hot_articles')
print(type(html))
print(html.read())
