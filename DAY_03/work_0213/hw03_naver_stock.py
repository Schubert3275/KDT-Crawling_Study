'''
과제 03. 네이버 시가 총액 top 20 기업 확인
- https://finance.naver.com/sise/sise_market_sum.naver

    <div id="contentarea">
    ...
    <tbody> 내부에 존재
        <a href="/item/main.naver?code=005930" class="title">삼성전자</a>

    - 이동할 URL
        'https://finance.naver.com' + '/item/main.naver?code=005930'
                                             ['href']속성의 값
'''
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

RANKING = 10
def get_top10_kospi_index(url, company_url_list, company_name_list):
    '''
    네이버 국내증시 > 시가총액 메뉴에서 시가총액 상위 10대 기업의 목록 크롤링
    - 각 회사의 네이터 URL 및 회사 이름 크롤링
    '''
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    tbody_tag = soup.find('tbody')
    company_links = tbody_tag.find_all('a', {'class': 'tltle'})

    for i in range(RANKING):
        url = 'https://finance.naver.com' + company_links[i]['href']
        company_name = company_links[i].text
        # 2개의 리스트에 추가함
        company_url_list.append(url)
        company_name_list.append(company_name)

def get_company_info(company_url):
    '''
    회사의 상세 정보를 가져옴
    <div id="middle class="new_totalinfo">
        <dl class="blind>
            <dt>종목 시세 정보</dt>
            <dd>종목명 삼성전자</dd>
            <dd>종목코드 005930 코스피</dd>
            <dd>현재가 61,330 전일대비 하락 500 마이너스 0.81 퍼센트</dd>
            <dd>전일가 61,800</dd>
            <dd>시가 61,800</dd>
            <dd>고가 62,200</dd>
            <dd>상한가 80,300</dd>
            <dd>저가 61,200</dd>
            <dd>하한가 43,300</dd>
            <dd>거래량 10,235,096</dd>
            <dd>거래대금 630,265백만</dd>
        </dl>
    '''

    stock_dict = dict({'종목명': '', '종목코드': '', '현재가': '', '전일가': '', '시가': '', '고가': '', '저가': ''})
    stock_dict_keys = stock_dict.keys()

    print(company_url)
    html = requests.get(company_url)

    soup = BeautifulSoup(html.text, 'html.parser')  # from_encoding='utf-8' 옵션 필요없음
    new_totalinfo_div = soup.find('dl', {'class':'blind'})

    # 각 dd 항목 분리
    dd_items = new_totalinfo_div.find_all('dd')

    for item in dd_items:
        item_list = item.text.split()
        key = item_list[0]
        value = item_list[1]
        # stock_dict 딕셔너리의 key에 해당하는 내용만 딕셔너리에 저장
        if key in stock_dict_keys:
            stock_dict[key] = value

    # 딕셔너리 내용 출력
    for key, value in stock_dict.items():
        print('{}: {}'.format(key, value))


def display_company_name(top_company_list):
    '''
    리스트에 저장된 코스피 상위 10대 기업의 이름을 출력
    '''
    print('-------------------------------------')
    print('[ 네이버 코스피 상위 {}대 기업 목록 ] '.format(RANKING))
    print('-------------------------------------')
    for i in range(len(top_company_list)):
        print('[{:2d}] {:30s}'.format(i+1, top_company_list[i]))


def main():
    naver_stock_url = 'https://finance.naver.com/sise/sise_market_sum.naver'
    top_url_list = [] # top10 회사의 Naver url 정보
    top_company_list = [] # top10 회사의 이름

    get_top10_kospi_index(naver_stock_url, top_url_list, top_company_list)
    #print(top_url_list)

    while True:
        display_company_name(top_company_list)
        choice = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
        if choice == -1:
            break
        # 선택한 기업의 url로 이동
        get_company_info(top_url_list[choice-1])

    print('프로그램 종료 ')

main()