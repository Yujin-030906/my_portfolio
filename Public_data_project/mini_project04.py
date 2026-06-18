import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

rain_df = pd.read_csv("전국 강수량 2000 ~ 2025.csv", encoding="cp949")
humid_df = pd.read_csv("전국 습도 2000 ~ 2025.csv", encoding="cp949")

rain_df.columns = rain_df.columns.str.strip()
humid_df.columns = humid_df.columns.str.strip()

print("강수량 컬럼 : ", rain_df.columns)
print("습도 컬럼 : ", humid_df.columns)

# 강수량
rain_df['일시'] = pd.to_datetime(rain_df['일시'])
rain_df['year'] = rain_df['일시'].dt.year

# 습도
humid_df['일시'] = pd.to_datetime(humid_df['일시'])
humid_df['year'] = humid_df['일시'].dt.year

# 1시간 최다강수량
rain_df['1시간최다강수량(mm)'] = pd.to_numeric(rain_df['1시간최다강수량(mm)'], errors='coerce')

# 평균 습도
humid_df['평균습도(%)'] = pd.to_numeric(humid_df['평균습도(%rh)'], errors='coerce')

HEAVY_RAIN = 80

heavy_rain_days = (rain_df[rain_df['1시간최다강수량(mm)'] >= HEAVY_RAIN].groupby('year').size().reset_index(name='폭우일수'))

yearly_humidity = (humid_df.groupby('year')['평균습도(%)'].mean().reset_index())

merged = pd.merge(yearly_humidity, heavy_rain_days, on='year', how='inner')

fig, ax1 = plt.subplots(figsize=(13, 6))

# 왼쪽 축: 습도
ax1.plot(merged['year'], merged['평균습도(%)'], marker='o', color='green', label='연평균 습도')
ax1.set_xlabel('연도')
ax1.set_ylabel('평균 습도 (%)', color='green')
ax1.tick_params(axis='y', labelcolor='green')

# 오른쪽 축: 폭우 일수
ax2 = ax1.twinx()
ax2.plot(merged['year'], merged['폭우일수'], marker='s', linestyle='--', color='blue', label='폭우 일수 (≥80mm)')
ax2.set_ylabel('폭우 일수 (일)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

plt.title('연도별 평균 습도와 폭우 발생 빈도 변화')

# 범례 통합
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.grid(True)
plt.show()