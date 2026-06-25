import os
import sys
import urllib.request
import json
import re
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

client_id = "yMgeXPfxfCLMRfAwmZkl"
client_secret = "gqyIz0YR0C"
encText = urllib.parse.quote("자율주행 연구개발 취업 자격증")
# stopwords = ['현대자동차', '현대', '자동차', '자율주행', '차', '자율', '주행', '현대차', '그룹', '사업', '전략', '확대', '추진', '협력', '강화', '중심', '관련', '이번', '발표', '기자', '지난', '통해', '테슬라']
# stopwords = ['기아자동차', '기아', '자동차', '자율주행', '차', '자율', '주행', '기아차', '그룹', '현대차', '현대', '사업', '전략', '확대', '추진', '협력', '강화', '중심', '관련', '이번', '발표', '기자', '지난', '통해', '테슬라', '차량', '시장', '산업', '지난해', '영역', '정의선', '한국', '모든', '사람', '출시', '사회']
# stopwords = ['한국지엠자동차', '한국지엠', '지엠', '자동차', '자율주행', '차', '자율', '주행', '한국', '사업', '전략', '확대', '추진', '협력', '강화', '중심', '관련', '이번', '발표', '기자', '지난', '통해', '현대', '협회', '산업', '국내', '코리아', '현대', '기아', '현대차', '단체', '차량', '대비', '지난해', '연합체', '시장', '업계', '협동', '주요', '전망', '센터', '정부', '인천', '투자', '테슬라', '행차', '동기', '그룹', '출시']
stopwords = ['우대', '사항', '취업', '자율주행', '자율', '주행', '자격증', '국가', '교육', '취득', '산업', '청년', '분야', '지원', '자동차', '자립', '준비']
url = f"https://openapi.naver.com/v1/search/news.json?query={encText}&display=100"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)

if response.getcode() == 200:
    data = json.loads(response.read().decode('utf-8'))
    raw_text = ""
    for item in data['items']:
        raw_text += item['title'] + " " + item['description']
else:
    print("Error Code:" + response.getcode())

# HTML 태그 제거
clean_text = re.sub('<[^<]+?>', '', raw_text) 
okt = Okt()
nouns = okt.nouns(clean_text)

# 한 글자 단어 제거 및 불용어 처리
words = [n for n in nouns if len(n) > 1 and n not in stopwords]
count = Counter(words)

font_path = 'C:/Windows/Fonts/malgun.ttf' 

img_mask = np.array(Image.open('image.png'))
wc = WordCloud(
    font_path=font_path,
    background_color='white',
    width=800,
    height=600,
    mask = img_mask
)
print(dict(count))
wc.generate_from_frequencies(dict(count))

plt.figure(figsize=(10, 8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()