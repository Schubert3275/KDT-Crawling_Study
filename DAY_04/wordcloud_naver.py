from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import platform
import numpy as np
from PIL import Image

def get_titles(start_num, end_num, search_word, title_list):
    while start_num <= end_num:
        url = (f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}&start={start_num}')
        # start_num ~ end_num까지 크롤링
        req = requests.get(url)
        time.sleep(1)
        if req.ok:  # 정상적인 request 확인
            soup = BeautifulSoup(req.text, 'html.parser')
            news_title = soup.find_all('a', {'class':'news_tit'})
            for news in news_title:
                title_list.append(news['title'])
        start_num += 10
        print('title 개수:', len(title_list))
        # print(title_list)


def make_wordcloud(title_list, stopwords, word_count):
    okt = Okt()
    sentences_tag = []
    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-' * 80)

    noun_adj_list = []
    # 명사와 형용사만 구분하여 리스트에 추가
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print('-' * 80)
    print(tags)

    tag_dict = dict(tags)
    # 검색어 제외 방법 2: dict에서 해당 검색어 제거
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)

    if platform.system() == 'Windows':
        path = path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac OS
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        path = r'/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'

    img_mask = np.array(Image.open('cloud.png'))
    wordcloud = WordCloud(font_path=path, width=800, height=800,
                          background_color='white', max_font_size=200,
                          repeat=True, colormap='inferno', mask=img_mask)

    cloud = wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


if __name__ == '__main__':
    search_word = "바이오 빅데이터"  # 검색어 지정
    title_list = []
    stopwords = [search_word, '데이터', '빅데이터', '플랫폼', '기반', '활용', '분석', '사례', '센터', '개최', '기업', '산업',
                 '바이오', '주가', '개발', '주차', '주식', '위']  # wordcloud에서 제외할 던어

    # 1~200번게시글까지 크롤링
    get_titles(1, 200, search_word, title_list)

    # 단어 50개까지 wordcloud로 출력
    make_wordcloud(title_list, stopwords, 50)
