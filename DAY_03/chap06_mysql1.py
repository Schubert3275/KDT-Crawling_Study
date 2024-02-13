"""
파이썬과 통합: 예제 #1
    ■ page 테이블에서 id값이 2인 데이터 가져오기
"""
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='scraping', charset='utf8')

cur = conn.cursor()
cur.execute('use scraping')
cur.execute('select * from pages where id=2')

print(cur.fetchone())
cur.close()
conn.close()
