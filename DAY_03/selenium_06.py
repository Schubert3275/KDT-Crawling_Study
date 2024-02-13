"""
동적 웹페이지 크롤링 예제 코드
"""
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script("storePop2(389)")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

driver.quit()
