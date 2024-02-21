## 크롤링

<details>
<summary>사용 교재</summary>

![](./images/파이썬으로%20웹%20크롤러%20만들기.png)

</details>

### DAY01

---

<details>
<summary> 데이터 크롤링과 정제: 크롤링 개념 </summary>

> -   웹 스크레이핑과 웹 크롤링 개념
> -   Beautiful Soup 소개
> -   HTML 구성 및 태그
> -   CSS 구성

</details>
<details>
<summary> 데이터 크롤링과 정제: Beautiful Soup 활용 </summary>

> -   Beautiful Soup 라이브러리 기초
> -   Beautiful Soup의 함수 활용

</details>

---

| 파일명                                   | 내용                                  |
| ---------------------------------------- | ------------------------------------- |
| `DAY_01\chap01.py`                       | 웹 페이지 가져오기                    |
| `DAY_01\chap01-bs01.py`                  | BeautifulSoup 라이브러리              |
| `DAY_01\chap01-bs03.py`                  | 존재하지 않는 태그 예외처리           |
| `DAY_01\chap01-bs04.py`                  | requests 모듈 사용 예제               |
| `DAY_01\chap01-request01.py`             | 멜론 웹사이트 접근 #1                 |
| `DAY_01\chap01-request02.py`             | 멜론 웹사이트 접근 #2                 |
| `DAY_01\chap01_h1_h6.html`               | HTML 글자 태그                        |
| `DAY_01\chap01_p_tag.html`               | 단락 구분 태그: \<p> ... \</p>        |
| `DAY_01\chap01_br_space.html`            | 줄 바꿈과 공백                        |
| `DAY_01\chap01_ahref.html`               | 링크 태그                             |
| `DAY_01\chap01_div.html`                 | 공간 분할 태그: div                   |
| `DAY_01\chap01_table.html`               | HTML Table 구성 태그                  |
| `DAY_01\chap01_css_ex.html`              | 고급 HTML 분석: CSS 스타일            |
| `DAY_01\chap02_bs.py`                    | BeautifulSoup 첫 예제                 |
| `DAY_01\chap02_bs02.py`                  | BeautifulSoup 기초                    |
| `DAY_01\chap02_bs03_find.py`             | BeautifulSoup 기초: find() 함수       |
| `DAY_01\chap02_bs04_mutivalued_class.py` | class 속성 예제                       |
| `DAY_01\chap02_bs05_findall.py`          | BeautifulSoup 기초: find_all() 함수   |
| `DAY_01\chap02_bs06_select.py`           | BeautifulSoup 기초: select_one() 함수 |
| `DAY_01\chap02_bs07_anthem.py`           | national_anthem 제목과 가사 내용 추출 |

#### DAY01 실습과제

---

    1. Weather Service
    2. 네이버 날씨

### DAY02

---

<details>
<summary> 데이터 크롤링과 정제: HTML 분석 및 정규식 </summary>

> -   HTML 분석
> -   정규 표현식

</details>
<details>
<summary> 데이터 크롤링과 정제: 크롤링 시작하기 </summary>

> -   단일 도메인 내의 이동
> -   전체 사이트 크롤링
> -   인터넷 크롤링

</details>

---

| 파일명                        | 내용                                              |
| ----------------------------- | ------------------------------------------------- |
| `DAY_02\chap03_html01.py`     | CSS 속성을 이용한 검색                            |
| `DAY_02\chap03_html04_03.py`  | 트리 이동: 형제 다루기 #1                         |
| `DAY_02\chap03_regex01.ipynb` | 정규 표현식                                       |
| `DAY_02\chap03_regex02.py`    | 정규 표현식과 BeautifulSoup #1                    |
| `DAY_02\chap03_regex03.py`    | 정규 표현식과 BeautifulSoup #2                    |
| `DAY_02\chap03_01.py`         | Wikipedia 페이지 가져오기                         |
| `DAY_02\chap03_02.py`         | 항목 링크 찾기                                    |
| `DAY_02\chap03_03.py`         | 링크간 무작위 이동하기: 소스코드                  |
| `DAY_02\chap03_04.py`         | 전체 사이트에서 데이터 수집                       |
| `DAY_02\chap03_05.py`         | 전체 사이트에서 데이터 수집: getLinks() 함수 수정 |
| `DAY_02\chap03_08_naver.py`   | 네이버 블로그 검색                                |

#### DAY02 실습과제

---

    1. 커피 매장 찾기
    2. 카드 게임

### DAY03

---

<details>
<summary> 데이터 크롤링과 정제: 데이터 저장 </summary>

> -   미디어 파일
> -   데이터를 CSV로 저장
> -   MySQL

</details>
<details>
<summary> 데이터 크롤링과 정제: 동적 웹페이지 크롤링 </summary>

> -   동적 웹페이지 크롤링 준비
> -   동적 웹페이지 크롤링

</details>
<details>
<summary> 데이터 크롤링과 정제: Naver Open API를 활용한 크롤링 </summary>

> -   Naver Open API 신청하기
> -   Open API를 활용한 크롤링

</details>

---

| 파일명                             | 내용                                               |
| ---------------------------------- | -------------------------------------------------- |
| `DAY_03\chap06_03.py`              | 데이터를 CSV 파일로 저장                           |
| `DAY_03\chap06_04.py`              | 테이블 데이터를 CSV로 저장                         |
| `DAY_03\chap06_04_01.py`           | 테이블 데이터를 CSV로 저장: html_table_parser 사용 |
| `DAY_03\chap06_mysql1.py`          | page 테이블에서 id값이 2인 데이터 가져오기         |
| `DAY_03\chap06_mysql2.py`          | 위키피디아의 자료를 MySQL에 저장                   |
| `DAY_03\chrome_driver_download.py` | chromedriver 자동 다운로드 소스                    |
| `DAY_03\selenium_01.py`            | Selenium 사용 #1                                   |
| `DAY_03\selenium_02.py`            | Selenium API: element 접근 예제 #1                 |
| `DAY_03\selenium_03_send_keys.py`  | Selenium API: 텍스트 입력 예제 (네이버 로그인)     |
| `DAY_03\selenium_04.py`            | Selenium API: 구글 검색어 입력 및 검색 결과        |
| `DAY_03\selenium_05.py`            | Selenium API: 프레임 이동 예제                     |
| `DAY_03\selenium_06.py`            | 동적 웹페이지 크롤링 예제 코드                     |
| `DAY_03\dhtml_coffeebean_01.py`    | 예제 코드1                                         |
| `DAY_03\dhtml_coffeebean_02.py`    | 예제 코드2                                         |
| `DAY_03\chap06_naverapi_ex01.py`   | 네이버 OpenAPI 사용: Python 샘플 코드              |
| `DAY_03\chap06_naverapi_ex02.py`   | 네이버 뉴스 검색: 단계 1                           |
| `DAY_03\chap06_naverapi_ex03.py`   | 네이버 뉴스 검색: 단계 2                           |

#### DAY03 실습과제

---

    1. 네이버 증시 정보 크롤링

### DAY04

---

<details>
<summary> 데이터 크롤링과 정제: 한국어 형태소 분석 </summary>

> -   자연어 처리
> -   크롤링 및 WordCloud 생성

</details>

---

| 파일명                      | 내용                               |
| --------------------------- | ---------------------------------- |
| `DAY_04\okt_01.py`          | Okt 간단 예제 #1                   |
| `DAY_04\okt_02.py`          | Okt 예제 #2                        |
| `DAY_04\wordcloud_01.py`    | 예제: 단어 분석 및 Word Cloud 생성 |
| `DAY_04\wordcloud_02.py`    | 영문 wordcloud 예제                |
| `DAY_04\wordcloud_naver.py` | 네이버 뉴스 타이틀 Word Cloud 예제 |
