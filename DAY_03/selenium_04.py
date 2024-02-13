"""
Selenium API: 구글 검색어 입력 및 검색 결과
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

# driver.implicitly_wait(5)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python')
search_box.submit()  # 검색 버튼 누름

time.sleep(10)
search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
print(len(search_results))

for result in search_results:
    title_element = result.find_element(By.CSS_SELECTOR, 'h3')
    title = title_element.text.strip()
    print(f"{title}")

driver.quit()
