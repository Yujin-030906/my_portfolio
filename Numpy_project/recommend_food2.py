import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

try:
    df = pd.read_csv('색상분류완료_v3.csv')
    # 콜레스테롤 컬럼 전처리 (문자열 제거 및 숫자 변환)
    df['콜레스테롤(mg)'] = pd.to_numeric(df['콜레스테롤(mg)'], errors='coerce').fillna(0)
    print("데이터 로드 및 전처리 성공!")
except FileNotFoundError:
    print("'색상분류완료_v3.csv' 파일을 찾을 수 없습니다.")
    df = pd.DataFrame({
        '식품명': ['마늘', '양파', '무', '버섯', '배추'],
        '색상구분': ['회색', '회색', '회색', '회색', '회색'],
        '콜레스테롤(mg)': [0, 0, 0, 0, 0]
    })

# '위험' 군 및 위험도별 추천 함수
def plot_caution_zone_recommendation(user_ldl, user_hdl):
    global df 
    
    user_lhr = user_ldl / user_hdl

    if user_lhr >= 2.5:
        status, target_color, limit, palette = "고위험", "초록", 0, "Greens_r"
        advice = "매우 높은 위험도! 콜레스테롤 0mg 초록색 식단 필수."
    elif 2.0 <= user_lhr < 2.5:
        status, target_color, limit, palette = "주의", "회색", 15, "Greys_r"
        advice = "주의 단계! 알리신이 풍부한 화이트/그레이 푸드 추천."
    else:
        status, target_color, limit, palette = "정상", "노랑", 35, "YlOrBr"
        advice = "정상 수치! 영양 균형이 잡힌 옐로우 푸드 추천."

    recommend_df = df[(df['색상구분'] == target_color) & (df['콜레스테롤(mg)'] <= limit)]

    if len(recommend_df) == 0:
        print(f"{target_color} 색상의 {limit}mg 이하 음식이 부족합니다. 저콜레스테롤 식단으로 대체합니다.")
        recommend_df = df[df['콜레스테롤(mg)'] <= 5]

    sample_df = recommend_df.sample(min(12, len(recommend_df)))
    sizes = [10] * len(sample_df)
    labels = [f"{name}\n({chol}mg)" for name, chol in zip(sample_df['식품명'], sample_df['콜레스테롤(mg)'])]

    plt.figure(figsize=(12, 8))
    squarify.plot(sizes=sizes, label=labels, alpha=0.8, 
                  color=sns.color_palette(palette, len(sample_df)),
                  text_kwargs={'fontsize': 15, 'fontweight': 'bold'})
    
    plt.title(f'[주의] 맞춤 추천 음식 트리맵', fontsize=20, pad=20)
    plt.figtext(0.5, 0.02, advice, ha="center", fontsize=15, color='darkblue', bbox={"facecolor":"white", "alpha":0.5, "pad":5})
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # LDL 140, HDL 60 -> LHR 2.33
    plot_caution_zone_recommendation(140, 60)