import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re

df = pd.read_csv('all_jobs_combined.csv')

keywords = [
    '석사', 'SLAM', 'LiDAR', 'Cloud', '알고리즘', 'ROS', 'C++', 'Python', 'Git', 'Eigen', 'PCL', 'OpenCV'
    '리눅스', 'AI', 'LLM', 'VLA'
    'LS-DYNA', 'PRIMER', 'HYPER-MESH'
    'C언어', '학사', 'CANoe', 'T32', 'CAN', 'HILS', 'MATLAB' '임베디드'
    'VLM', 'C/C++', '경험'
]

def count_keywords(text, kw_list):
    counts = {}
    text = str(text).upper()
    for kw in kw_list:
        if re.search(kw.upper(), text):
            counts[kw] = 1
        else:
            counts[kw] = 0
    return pd.Series(counts)

keyword_counts = df['description'].apply(lambda x: count_keywords(x, keywords))
total_counts = keyword_counts.sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
total_counts.plot(kind='bar', color='salmon')

plt.title('자동차 설계 채용 공고 주요 요구 역량 빈도수', fontsize=20)
plt.xlabel('역량 키워드')
plt.ylabel('언급된 공고 수')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()