import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

df = pd.read_csv('색상분류완료_v3.csv')

plt.figure(figsize=(12, 6))
sns.violinplot(x='색상구분', y='콜레스테롤(mg)', data=df, 
               palette={'초록': 'green', '빨강': 'red', '노랑': 'orange', '회색': 'gray', '흰색': 'white'})

plt.title('음식 색상별 콜레스테롤 함량 분포 (안전도 체크)', fontsize=15)
plt.axhline(y=10, color='blue', linestyle='--', label='저콜레스테롤 기준(10mg)')
plt.legend()
plt.show()