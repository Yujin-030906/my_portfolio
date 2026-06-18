# Crawling_project — 자동차·기계 분야 채용 공고 크롤링 및 요구 역량 분석

사람인·원티드·잡플래닛 채용 공고와 네이버 API 데이터를 크롤링해 자동차·기계 분야 취업에 필요한 기술 스택, 자격증, 기업 평점을 분석하고 시각화한 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 주제 |
|------|------|
| `job_url.py` | 사람인 채용 공고 Selenium 크롤링 → CSV 저장 |
| `wanted_final.py` | 원티드 채용 공고 목록·자격요건 크롤링 → CSV 저장 |
| `jobplanet.py` | 잡플래닛 기업 규모별 평점 크롤링 및 시각화 |
| `project_csv.py` | 수집된 CSV 파일 통합 (`all_jobs_combined.csv`) |
| `visualization_count.py` | 통합 공고 데이터 주요 역량 키워드 빈도 시각화 |
| `wanted_visualization.py` | 원티드 공고 기계 엔지니어 기술 스택 빈도 시각화 |
| `certification.py` | 네이버 블로그 API — 자동차 설계 기술·자격증 언급 빈도 시각화 |
| `project_naverapi_count.py` | 네이버 뉴스 API — 자율주행 관련 키워드 워드클라우드 생성 |

---

## 📊 수집 데이터

| 파일 | 내용 |
|------|------|
| `saramin_1.csv` ~ `saramin_7.csv` | 사람인 채용 공고 크롤링 결과 |
| `hyundai_jobs.csv` ~ `hyundai_jobs2.csv` | 현대자동차 채용 공고 크롤링 결과 |
| `all_jobs_combined.csv` | 사람인·현대자동차 공고 통합 파일 |
| `wanted_all_results.csv` | 원티드 공고 자격요건 크롤링 결과 |

---

## 📈 분석 내용

### job_url.py — 사람인 공고 크롤링

- Selenium으로 사람인 채용 공고 URL 접속
- iframe 전환 후 본문 텍스트 추출
- 공고별 URL·공고 내용을 CSV로 저장

### wanted_final.py — 원티드 공고 크롤링

- 원티드 자동차·기계 카테고리 목록 페이지 스크롤 크롤링
- 공고 카드에서 제목·링크 수집 후 각 상세 페이지 접속
- 자격요건 섹션만 추출해 CSV로 저장

### jobplanet.py — 기업 규모별 평점 비교

- 잡플래닛 기업 리뷰 페이지에서 대기업·중견기업·중소기업 9개사 평점 크롤링
- `sns.barplot()`으로 기업 규모별 평점 비교 시각화

### project_csv.py — 공고 데이터 통합

- 사람인·현대자동차 CSV 10개를 `pd.concat()`으로 통합
- `all_jobs_combined.csv`로 저장

### visualization_count.py — 역량 키워드 빈도 분석

- 통합 공고 본문에서 SLAM·LiDAR·ROS·C++·Python 등 키워드 정규식 매칭
- 키워드별 언급 공고 수를 막대 그래프로 시각화

### wanted_visualization.py — 기술 스택 빈도 분석

- 원티드 자격요건 텍스트에서 CAD·CATIA·ANSYS·Python 등 설계·코딩 도구 추출
- KoNLPy(`Okt`) 명사 추출과 정규식 결합 → `Counter`로 빈도 집계 → 상위 15개 시각화

### certification.py — 네이버 블로그 API 분석

- 네이버 블로그 검색 API로 "자동차 설계 프로그래밍 역량 자격증" 상위 100건 수집
- Python·C++·PLC·ROS·ISO26262 등 기술 스택·자격증 언급 빈도 시각화

### project_naverapi_count.py — 워드클라우드 생성

- 네이버 뉴스 API로 "자율주행 연구개발 취업 자격증" 상위 100건 수집
- KoNLPy 명사 추출 및 불용어 제거 후 이미지 마스크 기반 워드클라우드 생성

---

## 🛠 사용 기술

- **Python**
- **Selenium**
- **BeautifulSoup**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **KoNLPy**
- **WordCloud**
- **네이버 검색 API** (블로그·뉴스)
