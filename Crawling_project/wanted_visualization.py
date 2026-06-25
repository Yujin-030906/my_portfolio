import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from konlpy.tag import Okt

df = pd.read_csv('wanted_all_results.csv')
text_data = " ".join(df['자격요건'].astype(str))

target_keywords = [
    'CAD', 'AutoCAD', 'SolidWorks', 'CATIA', 'Inventor', 'NX', 'UG', 'Creo',
    'CAE', 'CFD', 'FEA', 'ANSYS', 'ABAQUS', 'MATLAB', 'Simulink',
    'Python', 'C++', 'Java', 'PLC', 'ROS', 'Linux', 'Arduino',
    '기구설계', '회로설계', '공정설계', '금형설계', '역설계', '모델링', '도면'
]

english_tools = re.findall(r'[A-Z][A-Za-z0-9#+]+', text_data)

okt = Okt()
nouns = okt.nouns(text_data)

extracted_words = []
for word in nouns + english_tools:
    if any(target.lower() == word.lower() for target in target_keywords):
        extracted_words.append(word.upper())

count = Counter(extracted_words)
top_tech = count.most_common(15)

chart_df = pd.DataFrame(top_tech, columns=['기술스택', '빈도수'])

plt.figure(figsize=(12, 8))
plt.rc('font', family='Malgun Gothic')
sns.barplot(x='빈도수', y='기술스택', data=chart_df, palette='magma')

plt.title('기계 엔지니어 공고 내 주요 설계 및 코딩 도구 빈도', fontsize=20)
plt.xlabel('언급된 공고 수')
plt.ylabel('기술/도구 명칭')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()