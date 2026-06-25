import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. 데이터 준비 (제공해주신 이미지 1, 4, 6번 통합 데이터 기반)
# 올리브영(ov)과 세탁소(ld) 데이터를 리스트로 정의합니다.
data = {
    'gu_name': ['서구', '남구', '동구', '달성군', '달서구', '북구', '수성구', '중구'],
    'ov_people_per_shop': [81978, 67771, 56547, 42443, 39774, 31527, 29230, 12626], # 프로젝트1.png
    'ld_people_per_shop': [1690, 1316, 2630, 3265, 2665, 2751, 2177, 2658],        # 프로젝트4.png
    'land_price': [950000, 1199000, 1050000, 450000, 1350000, 1100000, 1850000, 2500000] # 6.png 추정치
}
df = pd.DataFrame(data)

def draw_strategy_chart(df, x_col, y_col, title):
    plt.figure(figsize=(12, 8))
    sns.set_theme(style="whitegrid", font="Malgun Gothic")
    
    # 사분면 가이드 라인 (평균값 기준)
    x_mid = df[x_col].median()
    y_mid = df[y_col].median()
    
    # 1. 산점도 그리기
    scatter = sns.scatterplot(data=df, x=x_col, y=y_col, s=300, hue='gu_name', palette='Set2', edgecolors='black')
    
    # 2. 사분면 텍스트 추가 (사용자 제공 가이드라인 적용)
    plt.text(x_mid*1.5, y_mid*1.8, "2. 상권 좋음 / 비용 큼\n(자본력 필요)", fontsize=12, color='blue', ha='center')
    plt.text(x_mid*1.5, y_mid*0.5, "3. 경쟁 적음 / 비용 낮음 \n(최우선 후보)", fontsize=12, color='green', ha='center', fontweight='bold')
    plt.text(x_mid*0.5, y_mid*1.8, "1. 이미 포화 / 임대료 비쌈\n(창업 비추천)", fontsize=12, color='red', ha='center')
    plt.text(x_mid*0.5, y_mid*0.5, "4. 저가 경쟁 / 마진 박함\n(콘셉트 중요)", fontsize=12, color='orange', ha='center')

    # 가이드 점선
    plt.axvline(x_mid, color='gray', linestyle='--', alpha=0.5)
    plt.axhline(y_mid, color='gray', linestyle='--', alpha=0.5)

    # 그래프 꾸미기
    plt.title(title, fontsize=25, pad=20)
    plt.xlabel('매장당 인구 (수요: 높을수록 좋음)', fontsize=13)
    plt.ylabel('공시지가 (비용: 낮을수록 좋음)', fontsize=13)
    
    # 지역명 라벨링
    for i in range(df.shape[0]):
        plt.text(df[x_col][i], df[y_col][i]+50000, df.gu_name[i], ha='center', fontsize=10)

    plt.tight_layout()
    plt.show()

# --- 실행 ---
# 올리브영 전략 차트
draw_strategy_chart(df, 'ov_people_per_shop', 'land_price', '대구 올리브영 창업 전략 맵')

# 세탁소 전략 차트
draw_strategy_chart(df, 'ld_people_per_shop', 'land_price', '대구 세탁소 창업 전략 맵')