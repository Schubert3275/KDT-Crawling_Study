'''
저장된 hollys_branches.csv 파일을 읽어서 사용자가 입력한 지역에 존재하는 매장 검색 기능 구현
 - DataFrame으로 변경 후 DataFrame에서 값 검색 하기
'''

import pandas as pd

def search_branch(city):
    df = pd.read_csv('hollys_branches.csv', encoding='utf-8')
    # str.contains(문자열):  문자열을 포함하고 있는 컬럼 검색
    location_phone = df[df['위치(시,구)'].str.contains(city)]

    print(location_phone.columns)
    loc_phone_df = pd.DataFrame(location_phone, columns=('주소', '전화번호'))

    #
    # DataFrame을 list로 변경: values.tolist()
    #
    loc_phone_list = loc_phone_df.values.tolist()
    search_store_num = len(loc_phone_list)

    print('-' * 20)
    print('검색된 매장 수: ', search_store_num)
    print('-' * 20)

    if search_store_num == 0:
        print('검색된 매장이 없습니다.')
    else:
        count = 1
        for store in loc_phone_list:
            print('[{0:3d}]: {1}'.format(count, store))
            count += 1    
        print('-' * 100)
        print()

        
def main():
    city = ''
    # 검색할 시, 구 입력 ('quit' 입력시 프로그램 종료)
    while True:
        city = input('검색할 매장의 도시를 입력하세요: ')
        if(city == 'quit'):
            print('종료 합니다.')
            break
        else:
            search_branch(city)

main()
