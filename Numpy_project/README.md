# Numpy_project — 콜레스테롤 LHR 지수 기반 연령별 위험도 분석 및 맞춤 식단 추천

한국인 LDL·HDL 콜레스테롤 참조표준 데이터를 NumPy로 분석해 연령별 LHR 지수 추세를 예측하고, 위험도 구간에 따라 맞춤 식단을 추천하는 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 주제 |
|------|------|
| `np_chol2.py` | 한국인 남성 연령별 LHR 지수 추세 분석 (2차 다항식 회귀) |
| `np_chol3.py` | 한국인 여성 연령별 LHR 지수 추세 분석 (2차 다항식 회귀) |
| `cal_co2.py` | 남녀 연령별 LHR 지수 추이 비교 꺾은선 그래프 |
| `recommend.py` | LHR 구간별 음식 콜레스테롤 허용 가이드 시각화 |
| `recommend_food.py` | LHR 값 기반 맞춤 추천 음식 트리맵 (고위험) |
| `recommend_food2.py` | LHR 값 기반 맞춤 추천 음식 트리맵 (주의) |
| `no_food.py` | 고콜레스테롤 식품 TOP 15 트리맵 |
| `search_food2.py` | 음식 색상별 콜레스테롤 함량 분포 바이올린 플롯 |

---

## 📊 데이터 소스

- `한국인 LDL콜레스테롤 참조표준.csv` — 성별·지역·나이별 LDL 평균 측정값(mg/dL)
- `한국인 HDL콜레스테롤 참조표준.csv` — 성별·지역·나이별 HDL 평균 측정값(mg/dL)
- `한국인_연령별_LHR지수.csv` — 연령별·성별 LHR 지수 (LDL/HDL)
- `색상분류완료_v3.csv` — 식품명, 색상구분(초록/빨강/노랑/회색/흰색), 콜레스테롤 함량(mg)

---

## 📈 분석 내용

### np_chol2.py / np_chol3.py — 연령별 LHR 추세 예측

- LDL·HDL 참조표준 CSV를 연령 기준으로 `pd.merge()`
- `LHR = LDL / HDL`로 위험도 지수 계산
- `np.polyfit(x, y, 2)`으로 2차 다항식 회귀 계수 추출
- `np.poly1d()`로 예측 모델 생성 후 연령별 추세선 시각화
- 남성/여성 각각 분리 분석 (45세 예상 LHR 출력)

### cal_co2.py — 남녀 LHR 추이 비교

- 남녀 연령별 LHR 지수를 이중 꺾은선 그래프로 비교
- 주의(2.0), 고위험(2.5) 기준선을 `axhline()`으로 표시

### recommend.py — LHR 구간별 허용 가이드

- `np.linspace()`로 LHR 범위(1.0~4.0) 생성
- `np.select()`로 구간별 허용 콜레스테롤 허용치 분류
  - 정상(< 2.0): 35mg 이하 / 주의(2.0~2.5): 10mg 이하 / 고위험(≥ 2.5): 0mg
- `fill_between()` + `axvspan()`으로 구간별 색상 구분 시각화

### recommend_food.py / recommend_food2.py — 맞춤 식단 추천

- 사용자 LDL·HDL 입력 → LHR 계산 → 위험도 판정
- 위험도별 추천 색상 푸드 필터링 (초록: 0mg / 회색: 15mg / 노랑: 35mg 이하)
- `squarify.plot()`으로 추천 음식 트리맵 시각화

### no_food.py — 고콜레스테롤 식품 TOP 15

- 콜레스테롤 함량 기준 상위 15개 식품 추출
- 콜레스테롤 함량에 비례한 면적으로 트리맵 시각화

### search_food2.py — 색상별 콜레스테롤 분포

- 식품 색상 구분별 콜레스테롤 분포를 `sns.violinplot()`으로 시각화
- 저콜레스테롤 기준선(10mg) 표시

---

## 🛠 사용 기술

- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **squarify**
