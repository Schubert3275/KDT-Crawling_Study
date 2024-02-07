from urllib.request import urlopen
from bs4 import BeautifulSoup


def scraping_use_find(soup):
    forecast_list = soup.find('ul', {'id': 'seven-day-forecast-list'})
    forecast_tomstone = forecast_list.find_all('li', {'class': 'forecast-tombstone'})
    container_len = len(forecast_tomstone)

    print("[find 함수 사용]")
    print(f'총 tomestone-container 검색 개수: {container_len}')
    print('-' * 100)

    for i in range(container_len):
        period = forecast_tomstone[i].find('p', {'class': 'period-name'})
        short_desc = forecast_tomstone[i].find('p', {'class': 'short-desc'})
        temperature = forecast_tomstone[i].find('p', {'class': 'temp'})
        image_desc = forecast_tomstone[i].find('img', {'class': 'forecast-icon'})
        print_result(period, short_desc, temperature, image_desc)



def scraping_use_select(soup):
    forecast_list = soup.select_one('ul#seven-day-forecast-list')
    forecast_tomstone = forecast_list.select('li.forecast-tombstone')
    container_len = len(forecast_tomstone)

    print("[select 함수 사용]")
    print(f'총 tomestone-container 검색 개수: {container_len}')
    print('-' * 100)

    for i in range(container_len):
        period = forecast_tomstone[i].select_one('.period-name')
        short_desc = forecast_tomstone[i].select_one('.short-desc')
        temperature = forecast_tomstone[i].select_one('.temp')
        image_desc = forecast_tomstone[i].select_one('.forecast-icon')
        print_result(period, short_desc, temperature, image_desc)


def print_result(period, short_desc, temperature, image_desc):
    print('[Period]:', period.get_text() if period != None else 'None')
    print('[Short desc]:', short_desc.get_text() if short_desc != None else 'None')
    print('[Temperature]:', temperature.get_text() if temperature != None else 'None')
    print('[Image desc]:', image_desc['alt'] if image_desc['alt'] != '' else 'None')
    print('-' * 100)


def main():
    html = urlopen("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
    soup = BeautifulSoup(html, "html.parser")

    print("National Weather Service Scraping")
    print("------------------------------------")
    scraping_use_find(soup)
    print()
    scraping_use_select(soup)


if __name__ == '__main__':
    main()
