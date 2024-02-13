"""
Selenium 사용 #1
    ■ 사용하는 운영체제의 ChromeDriver 다운로드
        ● 압축해제 후 특정 경로에 저장
            - Windows 사용자: PATH가 설정된 폴더에 저장
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

print(driver.current_url)
print(driver.title)
print(driver.page_source)

driver.implicitly_wait(time_to_wait=5)
driver.close()
driver.quit()
