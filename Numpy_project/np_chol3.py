import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

try:
    ldl_df = pd.read_csv('한국인 LDL콜레스테롤 참조표준.csv', encoding='cp949')
    hdl_df = pd.read_csv('한국인 HDL콜레스테롤 참조표준.csv', encoding='cp949')

    ldl_m = ldl_df[(ldl_df['지역'] == '전국') & (ldl_df['성별'] == '여성')].copy()
    hdl_m = hdl_df[(hdl_df['지역'] == '전국') & (hdl_df['성별'] == '여성')].copy()

    ldl_m['age_num'] = ldl_m['나이(세)'].str.extract('(\d+)').astype(int)
    hdl_m['age_num'] = hdl_m['나이(세)'].str.extract('(\d+)').astype(int)

    ldl_m = ldl_m.rename(columns={'측정값평균(mg-dL)': 'ldl'})
    hdl_m = hdl_m.rename(columns={'측정값평균(mg-dL)': 'hdl'})

    merged = pd.merge(ldl_m[['age_num', 'ldl']], 
                      hdl_m[['age_num', 'hdl']], 
                      on='age_num')
    
    # LHR 계산 (LDL / HDL)
    merged['lhr'] = merged['ldl'] / merged['hdl']

    x = merged['age_num'].values
    y = merged['lhr'].values

    weights = np.polyfit(x, y, 2)
    model = np.poly1d(weights)

    plt.figure(figsize=(12, 7))
    plt.scatter(x, y, color='teal', label='실제 연령별 LHR 평균', s=50)

    x_range = np.linspace(x.min(), x.max(), 100)
    plt.plot(x_range, model(x_range), color='tomato', lw=3, label='나이별 LHR 추세 예측선')

    plt.title('한국인 여성 연령별 LHR 지수 추세 분석', fontsize=20)
    plt.xlabel('나이 (세)', fontsize=15)
    plt.ylabel('LHR 지수 (위험도)', fontsize=15)
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.show()

    print(f"성공적으로 분석되었습니다. 45세 여성 예상 LHR: {model(45):.2f}")

except Exception as e:
    print(f"오류가 발생했습니다: {e}")
    if 'ldl_df' in locals():
        print("LDL 파일 컬럼명:", ldl_df.columns.tolist())