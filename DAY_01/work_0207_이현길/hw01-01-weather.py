'''
데이터크롤링과 정제
과제 #1

National Weather Service 웹사이트 (샌프란시스코 지역)
- https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_use_find(html):
    '''
    find() 함수를 사용하여 html  내용을 크롤링
    :param html:
    :return:
    '''
    print('[find 함수 사용]')
    
    forecast_items = html.find_all(class_='tombstone-container') # list형태로 리턴
    print('총 tomestone-container 검색 개수: ', len(forecast_items))

    try:
        for day in forecast_items:
            period = day.find('p', {'class' : 'period-name'}).text
            img_desc = day.find('img')['title'] # img의 'title' 속성값 가져오기
            short_desc = day.find('p', class_='short-desc').text

            low_temp = day.find('p', class_='temp')
            if low_temp is not None:
                temp = low_temp.text
            else:
                temp = ""

            print('-' * 80)
            print('[Period]: {0}'.format(period))
            print('[Short desc]:  {0}'.format(short_desc))
            print('[Temperature]: {0}'.format(temp))
            print('[Image desc]: {0}'.format(img_desc))

    except AttributeError as e:
        print(e)
            

    print('-' * 80)

def parse_use_select(html):
    '''
    select 함수를 사용하여 html 내용을 크롤링
    '''
    print('[select 함수 사용]')
    forecast_items = html.select('.tombstone-container')
    print('총 tomestone-container 검색 개수: ', len(forecast_items))

    for day in forecast_items:        
        period = day.select_one('.period-name').text
        img_desc = day.select_one('img')['title']
        short_desc = day.select_one('.short-desc').text
        low_temp = day.find('p', class_='temp')
        if low_temp is not None:
            temp = low_temp.text
        else:
            temp = ""

        print('-' * 80)
        print('[Period]: {0}'.format(period))
        print('[Short desc]:  {0}'.format(short_desc))
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: {0}'.format(img_desc))


def main():
    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html = BeautifulSoup(page.read(), 'html.parser') # 전체 페이지

    print('National Weather Service Scraping')
    print('----------------------------------')

    parse_use_find(html)
    parse_use_select(html)

main()




