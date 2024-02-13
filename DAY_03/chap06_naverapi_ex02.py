"""
네이버 뉴스 검색: 단계 1
    ■ 단계 1: 100개의 뉴스 검색 및 json 데이터 출력
"""
import urllib.request
import datetime
import json


def get_request_url(url):
    client_id = "2LQgwXKXCSoNIfUWZaGP"
    client_secret = "MOmpKzWxAl"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")


def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    parameters = f"?query={query_string}&start={start}&display={display}"

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        # json 문자열을 Python 객체로 변환
        return json.loads(response)


def main():
    node = 'news'  # 크롤링 대상
    # search_test = input('검색어를 입력하세요: ')
    search_text = '인공지능'
    cnt = 0

    json_response = get_naver_search(node, search_text, 1, 100)
    if (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            print(f"[{cnt}]", end=" ")
            print(post['title'])
            print(post['description'])
            print(post['originallink'])
            print(post['link'])
            print(post['pubDate'])


if __name__ == '__main__':
    main()
