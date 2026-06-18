import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

rain_df = pd.read_csv("전국 강수량 2000 ~ 2025.csv", encoding="cp949")
temp_df = pd.read_csv("전국 기온 1997~2025.csv", encoding="cp949")

# 강수량
rain_df['일시'] = pd.to_datetime(rain_df['일시'])
rain_df['year'] = rain_df['일시'].dt.year
rain_df['1시간최다강수량(mm)'] = pd.to_numeric(rain_df['1시간최다강수량(mm)'], errors = 'coerce')

# 기온
temp_df['일시'] = pd.to_datetime(temp_df['일시'])
temp_df['year'] = temp_df['일시'].dt.year

# 폭우 기준 (mm)
HEAVY_RAIN = 80

heavy_rain_days = (rain_df[rain_df['1시간최다강수량(mm)'] >= HEAVY_RAIN].groupby('year').size().reset_index(name='폭우일수'))

yearly_temp = (temp_df.groupby('year')['평균기온(℃)'].mean().reset_index())

merged = pd.merge(yearly_temp, heavy_rain_days, on='year', how='inner')

fig, ax1 = plt.subplots(figsize=(13, 6))

# 왼쪽 축: 기온
ax1.plot(merged['year'], merged['평균기온(℃)'], marker='o', label='연평균 기온', color = 'red')
ax1.set_xlabel('연도')
ax1.set_ylabel('평균 기온 (℃)')
ax1.tick_params(axis='y')

# 오른쪽 축: 폭우 일수
ax2 = ax1.twinx()
ax2.plot(merged['year'], merged['폭우일수'], marker='s', linestyle='--', label='폭우 일수 (≥80mm)', color = 'blue')
ax2.set_ylabel('폭우 일수 (일)')
ax2.tick_params(axis='y')

plt.title('연도별 평균 기온과 폭우 발생 빈도 변화')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.grid(True)
plt.show()