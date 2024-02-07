
import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

# 방법 1: requests 모듈 사용

'''
url='https://search.naver.com/search.naver?query=대구+날씨'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
'''
city = input('지역명을 입력하세요: ')
# 방법 2: 한글 깨지는 문제 때문에 quote('한글') 사용
query = quote(f'{city}+날씨')
url='https://search.naver.com/search.naver?query=' + query

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

# 위치 
address_area = soup.find('div', {'class':'title_area _area_panel'})
address = address_area.find('h2', {'class':'title'}).text
print('현재 위치: ', address)

# 날씨 정보 
weather_data = soup.find('div', {'class':'weather_info'})

# 현재 온도 
weather_temp = weather_data.find('div', {'class': 'temperature_text'}).text.strip()
print('현재 온도: ', weather_temp)

# 날씨 상태 
weather_status = weather_data.find('span', {'class':'weather before_slash'}).text
print('날씨 상태: ', weather_status)

# 미세 먼지, 초미세 먼지, 자외선, 일출
# class="today_chart_list"
air = soup.find('ul', {'class':'today_chart_list'})

air_all_info = air.find_all('li', {'class':'item_today'})
print('공기 상태: ')
for info in air_all_info:
    print(info.text.strip())

# 날씨, 강수 
weather_time = soup.find_all('li', {'class': '_li'})
print('-----------------------')
print('시간대별 날씨 및 온도')
print('-----------------------')
for i in weather_time:
    print(i.text.strip())
