# Visualization_project — 대한민국 동계 올림픽 메달 데이터 분석 및 시각화

Matplotlib·Seaborn을 활용해 1992~2022년 대한민국 동계 올림픽 메달 데이터를 분석하고 다양한 형태로 시각화한 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 주제 |
|------|------|
| `project.ipynb` | 동계 올림픽 메달 집계 및 종목별 순위 분석 |
| `project2.ipynb` | 연도별 메달 추이 및 세계선수권 성적 상관관계 분석 |
| `project_visualization.ipynb` | 주요 분석 결과 시각화 정리 |

---

## 📊 데이터 소스

| 파일 | 설명 |
|------|------|
| `Olympic_Games_Medal_Tally.csv` | 대회별 국가별 메달 집계 |
| `Olympic_Athlete_Event_Results.csv` | 선수별 종목별 올림픽 결과 |
| `olympic_results.csv` | 올림픽 전체 결과 |
| `winter_korea_df_all_sports.csv` | 한국 동계 올림픽 전체 종목 데이터 |
| `korea_best_ranks_2011_2021_world_championships_wikipedia.csv` | 종목별 세계선수권 최고 순위 |

---

## 📈 분석 내용

### project.ipynb — 동계 올림픽 메달 집계 및 종목별 분석

- 대한민국 동계 올림픽 역대 메달 개수 순위 산출 (1위: 2018 평창, 17개)
- 단체전 중복 제거 후 종목별 금·은·동 누적 집계
- 상위 5개 종목 분석 (쇼트트랙 101개로 압도적 1위)
- 종목별 금·은·동 누적 막대 그래프 시각화

**사용 기술:** Python, Pandas, Matplotlib, Seaborn, koreanize-matplotlib

---

### project2.ipynb — 연도별 추이 및 세계선수권 상관관계 분석

- 역대 동계 올림픽 메달 획득 추이 (영역 그래프 + 꺾은선)
- 2014·2018·2022 최근 3개 대회 Top5 종목 메달 추이 (Seaborn lineplot)
- 연도별 금·은·동 barplot 및 종목별 누적 막대 그래프
- 쇼트트랙 세계선수권 순위 vs 올림픽 메달 수 이중 축(twinx) 그래프
- KDE 밀도 분석으로 메달 집중 시기 파악

**사용 기술:** Python, Pandas, Matplotlib, Seaborn, koreanize-matplotlib

---

### project_visualization.ipynb — 주요 시각화 정리

- 동계 올림픽 Top5 종목 누적 막대 그래프
- 역대 메달 추이 (영역+꺾은선 혼합)
- 연도별·종목별 메달 구성 비교

**사용 기술:** Python, Pandas, Matplotlib, koreanize-matplotlib
