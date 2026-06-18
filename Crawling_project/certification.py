import os
import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

client_id = "yMgeXPfxfCLMRfAwmZkl"
client_secret = "gqyIz0YR0C"

def get_naver_data(keyword):
    encText = urllib.parse.quote(keyword)
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}&display=100"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8')) if response.getcode() == 200 else None

target_keywords = {
    'Python': '데이터/AI', 'C++': '임베디드/제어', 'C언어': '임베디드/제어',
    'PLC': '공정제어', 'MATLAB': '모델링/시뮬레이션', 'Simulink': '모델링/시뮬레이션',
    '정보처리기사': '자격증', 'ADsP': '자격증', '임베디드기사': '자격증',
    'ROS': '로봇/자율주행', 'ISO26262': '차량표준', 'AUTOSAR': '차량표준'
}

search_keyword = "자동차 설계 프로그래밍 역량 자격증"
result = get_naver_data(search_keyword)
found_words = []

if result:
    for item in result['items']:
        content = (item['title'] + " " + item['description']).upper()
        for key in target_keywords.keys():
            if key.upper() in content:
                found_words.append(key)

word_counts = Counter(found_words)
df_plot = pd.DataFrame(word_counts.most_common(), columns=['항목', '빈도수'])
df_plot['분류'] = df_plot['항목'].map(target_keywords)

plt.figure(figsize=(12, 8))
plt.rc('font', family='Malgun Gothic') 
sns.barplot(x='빈도수', y='항목', hue='분류', data=df_plot, dodge=False, palette='viridis')

plt.title(f"자동차 설계 분야 요구 프로그래밍/SW 역량 빈도", fontsize=18)
plt.xlabel("블로그 언급 횟수 (상위 100건 기준)")
plt.ylabel("기술 스택 / 자격증")
plt.legend(title='직무 분야', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()