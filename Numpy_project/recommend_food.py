import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

try:
    df = pd.read_csv('색상분류완료_v3.csv')
    df['콜레스테롤(mg)'] = pd.to_numeric(df['콜레스테롤(mg)'], errors='coerce').fillna(0)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 경로를 확인해주세요.")

def plot_treemap_recommendation(user_ldl, user_hdl):
    user_lhr = user_ldl / user_hdl

    if user_lhr >= 2.5:
        target_color, limit, status, palette = '초록', 0, '고위험', 'Greens_r'
    elif user_lhr >= 2.0:
        target_color, limit, status, palette = '회색', 15, '주의', 'Greys_r'
    else:
        target_color, limit, status, palette = '노랑', 35, '정상', 'YlOrBr'

    target_df = df[(df['색상구분'] == target_color) & (df['콜레스테롤(mg)'] <= limit)]

    if len(target_df) == 0:
        print(f"[{status}] 단계에 맞는 음식이 데이터에 없습니다.")
        return

    sample_size = min(15, len(target_df))
    target_df = target_df.sample(sample_size)

    plt.figure(figsize=(14, 9))

    sizes = [10] * len(target_df) # 모든 칸의 크기를 동일하게 배분
    labels = [f"{name}\n({chol}mg)" for name, chol in zip(target_df['식품명'], target_df['콜레스테롤(mg)'])]

    squarify.plot(sizes=sizes, label=labels, alpha=0.8, 
                  color=sns.color_palette(palette, len(target_df)),
                  text_kwargs={'fontsize': 20, 'fontweight': 'bold'})
    
    plt.title(f'[고위험] 맞춤 추천 음식 트리맵', fontsize=20, pad=20)
    plt.axis('off')

    plt.figtext(0.5, 0.05, f"추천 기준: {target_color}색 푸드 / 콜레스테롤 {limit}mg 이하", 
                ha="center", fontsize=15, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})
    
    plt.tight_layout()
    plt.show()

plot_treemap_recommendation(user_ldl=160, user_hdl=45)