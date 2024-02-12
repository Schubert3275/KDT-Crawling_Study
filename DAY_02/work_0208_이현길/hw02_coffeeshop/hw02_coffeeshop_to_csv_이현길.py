from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

storeDF = pd.DataFrame(columns=["매장이름", "위치(시,구)", "주소", "전화번호"])
file = "hollys_branches.csv"

num = 0
for i in range(1, 52):
    try:
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')

        contents = bs.select_one("#contents")
        tb_store = contents.select(".tb_store tbody tr")
        for tr in tb_store:
            num += 1
            center_t = tr.select(".center_t")
            area = center_t[0].text.strip()
            store_name = center_t[1].text.strip()
            address = center_t[3].text.strip()
            phone_number = center_t[5].text.strip()
            print(f'[{num:3}]: 매장이름: {store_name}, 지역: {area}, 주소: {address}, 전화번호: {phone_number}')
            storeDF.loc[num-1] = [store_name, area, address, phone_number]
    except Exception as e:
        print(e)
print(f'전체 매장 수 : {num}')

storeDF.to_csv(file, encoding="utf-8", mode="w", index=False)
print(f'{file} 파일 저장 완료')
