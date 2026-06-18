import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

rain_df = pd.read_csv("전국 강수량 2000 ~ 2025.csv", encoding="cp949")
temp_df = pd.read_csv("전국 기온 1997~2025.csv", encoding="cp949")
humid_df = pd.read_csv("전국 습도 2000 ~ 2025.csv", encoding="cp949")

rain_df.columns = rain_df.columns.str.strip()
temp_df.columns = temp_df.columns.str.strip()
humid_df.columns = humid_df.columns.str.strip()

print("강수량 컬럼:", rain_df.columns)
print("기온 컬럼:", temp_df.columns)
print("습도 컬럼:", humid_df.columns)

rain_date = [c for c in rain_df.columns if '일시' in c][0]
temp_date = [c for c in temp_df.columns if '일시' in c][0]
humid_date = [c for c in humid_df.columns if '일시' in c][0]

rain_df[rain_date] = pd.to_datetime(rain_df[rain_date])
temp_df[temp_date] = pd.to_datetime(temp_df[temp_date])
humid_df[humid_date] = pd.to_datetime(humid_df[humid_date])

rain_df['1시간최다강수량(mm)'] = pd.to_numeric(rain_df['1시간최다강수량(mm)'], errors='coerce')

temp_df['평균기온(℃)'] = pd.to_numeric(temp_df['평균기온(℃)'], errors='coerce')

humid_df['평균습도(%)'] = pd.to_numeric(humid_df['평균습도(%rh)'], errors='coerce')

rain_df['date'] = rain_df[rain_date].dt.date
temp_df['date'] = temp_df[temp_date].dt.date
humid_df['date'] = humid_df[humid_date].dt.date

rain_daily = rain_df.groupby('date')['1시간최다강수량(mm)'].max().reset_index()
temp_daily = temp_df.groupby('date')['평균기온(℃)'].mean().reset_index()
humid_daily = humid_df.groupby('date')['평균습도(%)'].mean().reset_index()

df = (rain_daily.merge(temp_daily, on='date').merge(humid_daily, on='date'))

print(df.head())

plt.figure(figsize=(10, 6))

sc = plt.scatter(df['평균기온(℃)'], df['1시간최다강수량(mm)'], c=df['평균습도(%)'], alpha=0.6)

plt.colorbar(sc, label='평균 습도 (%)')
plt.xlabel('평균 기온 (℃)')
plt.ylabel('1시간 최다강수량 (mm)')
plt.title('기온, 습도 vs 강수량')
plt.grid(True)
plt.show()