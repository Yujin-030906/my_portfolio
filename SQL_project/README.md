# SQL_project — 대구 공공데이터 기반 창업 입지 분석

대구광역시 세탁소·올리브영 점포 현황, 구별 인구, 공시지가 데이터를 SQL로 가공·분석하고, 창업 전략 맵을 시각화한 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 주제 |
|------|------|
| `laundry.py` | 세탁소 데이터 전처리 (Excel → CSV, 구별 ID 매핑) |
| `oliveyoung.py` | 올리브영 데이터 전처리 (Excel → CSV, 구별 ID 매핑) |
| `laundry_population_dalseo.sql` | 구별 인구 대비 세탁소 밀도 분석 |
| `oliveyoung_population_dalseo.sql` | 구별 인구 대비 올리브영 밀도 분석 |
| `namgu_areamoney.sql` | 남구 동별 인구·공시지가 조인 분석 |
| `project2.py` | 창업 전략 맵 시각화 (사분면 차트) |

---

## 📊 데이터 소스

- 대구광역시 세탁소 현황 공공데이터 (`laundry.xlsx`)
- 대구광역시 올리브영 점포 현황 공공데이터 (`oliveyoung.xlsx`)
- 대구광역시 구별 인구 데이터
- 대구광역시 남구 동별 공시지가 데이터

---

## 📈 분석 내용

### laundry.py / oliveyoung.py — 데이터 전처리

- 공공데이터 Excel 파일에서 필요한 컬럼(번호, 주소, 사업장명) 추출
- 정규식으로 대구광역시 구·동 정보 파싱
- 구별 ID(`dong_id`) 매핑 후 CSV로 저장

### laundry_population_dalseo.sql — 세탁소 밀도 분석

- `daegu` 테이블(구별 인구)과 `laundry_daegu` 테이블 LEFT JOIN
- 구별 세탁소 수 집계 및 `인구 / 점포 수` 계산으로 매장당 담당 인구 산출
- "인구 대비 세탁소가 가장 적은 구"(수요 높은 입지) 파악

### oliveyoung_population_dalseo.sql — 올리브영 밀도 분석

- 동일한 방식으로 올리브영 점포 밀도 분석
- 구별 매장당 인구 순위 산출

### namgu_areamoney.sql — 남구 공시지가 분석

- `namgu`(인구)와 `land_value_with_code`(공시지가) INNER JOIN
- 동 이름 기반 매핑으로 동별 인구·공시지가 통합 조회
- 공시지가 오름차순 정렬로 저비용 입지 파악

### project2.py — 창업 전략 맵 시각화

- 올리브영·세탁소 각각 매장당 인구(수요) vs 공시지가(비용) 산점도
- 중앙값 기준 4개 사분면으로 창업 입지 전략 분류
  - **3사분면(수요↑, 비용↓)**: 최우선 창업 후보
  - **1사분면(수요↓, 비용↑)**: 창업 비추천

---

## 🛠 사용 기술

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **SQL (MySQL)**
