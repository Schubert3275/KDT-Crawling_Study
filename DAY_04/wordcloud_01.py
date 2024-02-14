"""
예제: 단어 분석 및 Word Cloud 생성
"""
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

text = open('test.txt', encoding='utf-8').read()
okt = Okt()  # Open Korean Text 객체 생성

# okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag = []
sentences_tag = okt.pos(text)

noun_adj_list = []
# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)
# 가장 많이 나온 단어 50개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(50)
print(tags)

# 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, window는 .ttf 파일의 위치를 지정
if platform.system() == 'Windows':
    path = r'C:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':  # Mac OS
    path = r'/System/Library/Fonts/AppleGothic'
else:
    path = r'/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'

img_mask = np.array(Image.open('cloud.png'))

wc1 = WordCloud(font_path=path, width=400, height=400,
               background_color='white', max_font_size=200,
               repeat=False, colormap='inferno', mask=img_mask)

wc2 = WordCloud(font_path=path, width=400, height=400,
               background_color='white', max_font_size=200,
               repeat=True, colormap='inferno', mask=img_mask)

cloud1 = wc1.generate_from_frequencies(dict(tags))
cloud2 = wc2.generate_from_frequencies(dict(tags))
# 생성된 WordCloud를 test.jpg로 보낸다
# cloud.to_file('test.jpg')
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
plt.axis('off')
plt.imshow(cloud1)
plt.title('repeat=False', y=-0.2)
plt.subplot(1, 2, 2)
plt.axis('off')
plt.imshow(cloud2)
plt.title('repeat=True', y=-0.2)
plt.show()
