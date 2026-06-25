import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

rain_df = pd.read_csv("전국 강수량 2000 ~ 2025.csv", encoding="cp949")

rain_df['일시'] = pd.to_datetime(rain_df['일시'])
rain_df['year'] = rain_df['일시'].dt.year

rain_df['1시간최다강수량(mm)'] = pd.to_numeric(rain_df['1시간최다강수량(mm)'], errors='coerce')

# 결측값 제거
rain_df = rain_df.dropna(subset=['1시간최다강수량(mm)'])

years = sorted(rain_df['year'].unique())

boxplot_data = [rain_df[rain_df['year'] == y]['1시간최다강수량(mm)'] for y in years]

plt.figure(figsize=(15, 7))

plt.boxplot(boxplot_data, labels=years, showfliers=True)

plt.title('연도별 1시간 동안 내리는 최대강수량 분포 변화')
plt.xlabel('연도')
plt.ylabel('1시간 최다강수량 (mm)')

plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()