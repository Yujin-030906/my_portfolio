import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def get_review_score(company_dict):
    driver = webdriver.Chrome()
    data = []

    company_names = list(company_dict.keys())
    
    for i, name in enumerate(company_names):
        url = company_dict[name]
        driver.get(url)
        time.sleep(3)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        if i < 3:
            category = '대기업'
        elif i < 6:
            category = '중견기업'
        else:
            category = '중소기업'
            
        try:
            # 전체 평점 추출 (없을 경우 대비 예외처리)
            total_score_el = soup.select_one('span.rate_point')
            total_score = float(total_score_el.text) if total_score_el else 0.0

            data.append({
                '기업명': name,
                '분류': category,
                '평점': total_score
            })
            print(f"{name} ({category}): {total_score} 완료")
            
        except Exception as e:
            print(f"{name} 데이터 수집 중 오류: {e}")
            
    driver.quit()
    return pd.DataFrame(data)

def visualize_scores(df):
    plt.figure(figsize=(12, 6))

    sns.barplot(data=df, x='기업명', y='평점', hue='분류', palette='viridis')
    
    plt.title('기업 규모별 평점 비교', fontsize=20)
    plt.xlabel('기업명', fontsize=12)
    plt.ylabel('평점 (5.0 만점)', fontsize=12)
    plt.ylim(0, 5) # 평점 범위 고정
    plt.legend(title='기업 규모')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, row in df.iterrows():
        plt.text(i, row['평점'] + 0.1, f"{row['평점']}", ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()

company_dict = {
    '현대자동차': 'https://www.jobplanet.co.kr/companies/1289/reviews/현대자동차',
    '기아': 'https://www.jobplanet.co.kr/companies/43248/reviews/기아',
    '한국지엠': 'https://www.jobplanet.co.kr/companies/3079/reviews/한국지엠',
    '에스엘': 'https://www.jobplanet.co.kr/companies/20826/reviews/에스엘',
    '화신': 'https://www.jobplanet.co.kr/companies/47253/reviews/화신',
    '모트렉스': 'https://www.jobplanet.co.kr/companies/91467/reviews/모트렉스',
    '아진산업': 'https://www.jobplanet.co.kr/companies/22086/reviews/아진산업',
    '진양오일씰': 'https://www.jobplanet.co.kr/companies/54872/reviews/진양오일씰',
    '한신기계공업': 'https://www.jobplanet.co.kr/companies/2378/reviews/한신기계공업'
}

score_df = get_review_score(company_dict)

if not score_df.empty:
    visualize_scores(score_df)
    avg_df = score_df.groupby('분류')['평점'].mean()
    print("\n[규모별 평균 평점]")
    print(avg_df)