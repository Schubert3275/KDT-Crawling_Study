"""
예제 코드2
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


def coffeebean_store(store_list: list):
    coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome()

    for i in range(1, 388):
        driver.get(coffeebean_url)
        time.sleep(1)

        driver.execute_script(f'storePop2({i})')
        time.sleep(1)
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            store_name = soup.select('div.store_txt > h2').text
            store_info = soup.select(
                'div.store_txt > table.store_table > tboby > tr > td')
            store_address_list = list(store_info[2])
            store_addr = store_address_list[0]
            store_phone = store_info[3].text
            print(f'{i+1} {store_name} {store_addr} {store_phone}')
            store_list.append([store_name, store_addr, store_phone])
        except:
            continue
    driver.quit()


def main():
    store_info = []
    coffeebean_store(store_info)

    coffeebean_table = pd.DataFrame(store_info, columns=['매장이름', '주소', '전화번호'])
    print(coffeebean_table.head())

    coffeebean_table.to_csv('coffeebean_branches.csv',
                            encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':
    main()
