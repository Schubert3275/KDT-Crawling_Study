from selenium import webdriver
from selenium.webdriver.common.by import By
import re


def get_company_list(nameList: list, linkList: list):
    """
    1위부터 10위까지를 조회하여 종목명과 url를 리스트에 추가

    nameList: 종목명 리스트
    linkList: url 리스트
    """
    driver = webdriver.Chrome()
    driver.get("https://finance.naver.com/sise/sise_market_sum.naver")

    contentarea = driver.find_element(By.ID, 'contentarea')
    tr_links = contentarea.find_elements(By.CSS_SELECTOR, 'div.box_type_l > table.type_2 > tbody > tr >  td:nth-child(2) > a')

    for tr_link in tr_links[:10]:  # 10위까지만 저장
        nameList.append(tr_link.text)
        linkList.append(tr_link.get_attribute('href'))

    driver.quit()


def show_company_info(name: str, link: str):
    """
    주어진 url로 접속해 해당 종목의 데이터 출력

    name: 종목명
    link: 접속할 url
    """
    driver = webdriver.Chrome()
    driver.get(link)
    regex = re.compile('(?<=code=).+$')

    current_price = driver.find_elements(By.XPATH, '//*[@id="chart_area"]/div[1]/div/p[1]/em/span')
    previous_price = driver.find_elements(By.XPATH, '//*[@id="chart_area"]/div[1]/table/tbody/tr[1]/td[1]/em/span')
    opening_price = driver.find_elements(By.XPATH, '//*[@id="chart_area"]/div[1]/table/tbody/tr[2]/td[1]/em/span')
    highest_price = driver.find_elements(By.XPATH, '//*[@id="chart_area"]/div[1]/table/tbody/tr[1]/td[2]/em[1]/span')
    lowest_price = driver.find_elements(By.XPATH, '//*[@id="chart_area"]/div[1]/table/tbody/tr[2]/td[2]/em[1]/span')

    print(link)
    print('종목명:', name)
    print('종목코드:', regex.search(link).group())
    print('현재가:', ''.join(map(lambda x: x.text, current_price)))
    print('전일가:', ''.join(map(lambda x: x.text, previous_price)))
    print('시가:', ''.join(map(lambda x: x.text, opening_price)))
    print('고가:', ''.join(map(lambda x: x.text, highest_price)))
    print('저가:', ''.join(map(lambda x: x.text, lowest_price)))

    driver.quit()


def main():
    """
    셀레니움 활용
    """
    nameList = []
    linkList = []
    get_company_list(nameList, linkList)

    while True:
        print('-' * 37)
        print("[ 네이버 코스피 상위 10대 기업 목록 ]")
        print('-' * 37)

        for i in range(len(nameList)):
            print(f"[{i+1:2}] {nameList[i]}")

        number = input("주가를 검색할 기업의 번호를 입력하세요(-1: 종료): ")
        try:
            number = int(number)
        except:
            print("숫자를 입력하세요.")
            continue

        if number == -1:
            break
        elif 1 <= number <= 10:
            name = nameList[number-1]
            link = linkList[number-1]
            show_company_info(name, link)
        else:
            print("1~10 사이의 숫자를 입력하세요.")


if __name__ == "__main__":
    main()
