"""
존재하지 않는 태그 예외처리
"""
# ■ 존재하지 않는 태그 접근
#   ● None 객체 반환
#   ● None 객체에 접근: AtrributeError 발생
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        value = bsObj.body.find(tag)
    except AttributeError as e:
        return None
    return value


tag = 'h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)

if value == None:
    print(f'{tag} could not be found')
else:
    print(value)
