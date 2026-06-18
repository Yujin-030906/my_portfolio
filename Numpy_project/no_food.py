import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import koreanize_matplotlib

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

try:
    df = pd.read_csv('색상분류완료_v3.csv')
    df['콜레스테롤(mg)'] = pd.to_numeric(df['콜레스테롤(mg)'], errors='coerce').fillna(0)
    print("데이터 로드 성공")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 경로를 확인해주세요.")

def plot_danger_food_treemap():
    global df
    
    # 콜레스테롤이 높은 순서대로 15개 추출
    danger_df = df.sort_values(by='콜레스테롤(mg)', ascending=False).head(15)

    if len(danger_df) == 0:
        print("데이터가 비어있습니다.")
        return

    plt.figure(figsize=(14, 9))
    
    # 함량이 높을수록 면적이 커지도록 설정
    sizes = danger_df['콜레스테롤(mg)'].values
    labels = [f"{name}\n({chol}mg)" for name, chol in zip(danger_df['식품명'], danger_df['콜레스테롤(mg)'])]

    color_map = {'빨강': 'crimson', '초록': 'forestgreen', '노랑': 'orange', '회색': 'gray', '흰색': 'silver'}
    colors = [color_map.get(c, 'skyblue') for c in danger_df['색상구분']]

    color_map = {'빨강': 'crimson', '초록': 'forestgreen', '노랑': 'orange', '회색': 'gray', '흰색': 'silver'}
    colors = [color_map.get(c, 'skyblue') for c in danger_df['색상구분']]

    squarify.plot(sizes=sizes, label=labels, alpha=0.8, color=colors,
              text_kwargs={'fontsize': 20, 'fontweight': 'bold'})

    squarify.plot(sizes=sizes, label=labels, alpha=0.8, color=colors,
                  text_kwargs={'fontsize': 20, 'fontweight': 'bold'})
    
    plt.title('고콜레스테롤 식품 TOP 15', fontsize=20, pad=20, color='darkred')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_danger_food_treemap()