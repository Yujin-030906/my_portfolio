import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('한국인_연령별_LHR지수.csv')

national_df = df[df['지역'] == '전국'].copy()

plt.figure(figsize=(14, 7))

sns.lineplot(data=national_df, x='나이(세)', y='LHR_지수', hue='성별', 
             marker='o', linewidth=2, palette=['#1f77b4', '#d62728'])

plt.axhline(y=2.0, color='orange', linestyle='--', label='주의 (2.0)')
plt.axhline(y=2.5, color='red', linestyle='--', label='고위험 (2.5)')

plt.title('한국인 연령별 콜레스테롤 위험도(LHR 지수) 추이', fontsize=20, pad=20)
plt.xlabel('연령대', fontsize=15)
plt.ylabel('LHR 지수 (LDL/HDL)', fontsize=15)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.show()