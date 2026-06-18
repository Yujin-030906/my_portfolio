import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    list_url = 'https://www.wanted.co.kr/wdlist/513/843?country=kr&job_sort=job.popularity_order&years=-1&locations=all'
    driver.get(list_url)
    print("목록 페이지 로딩 중...")
    time.sleep(5)

    # 스크롤 내리기
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    job_cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-cy="job-card"]')
    print(f"발견된 공고 요소 개수: {len(job_cards)}개")

    job_list = []
    for card in job_cards:
        try:
            if card.tag_name == 'a':
                link = card.get_attribute('href')
            else:
                link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
            
            # 제목 추출
            title = card.text.split('\n')[0] 
            
            if link:
                job_list.append({'title': title, 'link': link})
        except Exception as e:
            continue

    print(f"최종 {len(job_list)}개의 링크 수집 완료. 상세 분석을 시작합니다.")
    print("-" * 50)

    final_results = []
    for idx, job in enumerate(job_list[:80], 1): 
        print(f"[{idx}/{len(job_list[:80])}] 분석 중: {job['title']}")
        driver.get(job['link'])
        time.sleep(4)

        try:
            container = driver.find_element(By.CSS_SELECTOR, '[class*="JobContent_descriptionWrapper"]')
            full_text = container.text
            
            if "자격요건" in full_text:
                temp_text = full_text.split("자격요건")[1]
                end_markers = ["우대사항", "혜택 및 복지", "기술스택", "채용 절차", "복리후생"]
                end_pos = len(temp_text)
                
                for marker in end_markers:
                    m_pos = temp_text.find(marker)
                    if m_pos != -1 and m_pos < end_pos:
                        end_pos = m_pos
                requirements = temp_text[:end_pos].strip()
            else:
                requirements = "자격요건 키워드 없음"

            final_results.append([job['title'], job['link'], requirements])
            print("   -> 성공")
        except:
            print("   -> 실패")
            final_results.append([job['title'], job['link'], "추출 실패"])

    if final_results:
        with open("wanted_all_results.csv", 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['공고명', '링크', '자격요건'])
            writer.writerows(final_results)
        print(f"\n[완료] 'wanted_all_results.csv' 파일이 저장되었습니다.")

finally:
    driver.quit()