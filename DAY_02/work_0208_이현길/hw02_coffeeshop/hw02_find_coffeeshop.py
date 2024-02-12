import pandas as pd

file = "hollys_branches.csv"
storeDF = pd.read_csv(file)

while True:
    print('-' * 20)
    city = input("검색할 매장의 도시를 입력하세요(quit 입력으로 종료): ")
    if city == 'quit':
        print("종료합니다.")
        break
    serchDF = storeDF[storeDF['위치(시,구)'].str.contains(city)]
    serchDF = serchDF[['주소', '전화번호']]
    num = serchDF.shape[0]
    print('-' * 20)
    print(f'검색된 매장 수:  {num}')
    print('-' * 20)
    for i in range(num):
        print(f'[{i+1:3}] : {serchDF.iloc[i].to_list()}')
