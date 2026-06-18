import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

file_path = "전국 강수량 2000 ~ 2025.csv"

df = pd.read_csv(file_path, encoding = 'cp949')

df['일시'] = pd.to_datetime(df['일시'])
df['year'] = df['일시'].dt.year

# 연도별 총 강수량
yearly_rainfall = (df.groupby('year')['평균일강수량(mm)'].sum().reset_index())

plt.figure(figsize=(12, 6))
plt.plot(yearly_rainfall['year'], yearly_rainfall['평균일강수량(mm)'], marker='o')

plt.title('2000~2025 연도별 총 강수량 변화')
plt.xlabel('연도')
plt.ylabel('총 강수량 (mm)')
plt.grid(True)

plt.show()