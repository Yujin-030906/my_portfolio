# Vision_project — MVTec Pill 비지도 학습 기반 불량 검출

MVTec Anomaly Detection Dataset의 **pill** 카테고리를 사용하여 정상 이미지만으로 학습한 뒤, PCA 재구성 오차 및 Isolation Forest를 활용해 불량을 탐지하는 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 내용 |
|------|------|
| `pill_data_final.ipynb` | 데이터 로딩 · EDA · HOG/HSV 특징 추출 · PCA 분석 · 모델 학습 및 평가 전체 파이프라인 |
| `pill_if.ipynb` | Isolation Forest 집중 실험 · 파라미터 튜닝 · PCA+IF 결합 모델 비교 |
| `*.png` | 혼동 행렬, 불량 Recall 히트맵, 임계값 분석, 케이스 스터디 등 결과 시각화 |

---

## 📊 데이터 소스

- **MVTec Anomaly Detection Dataset — Pill**
  - 출처: [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad)
  - 구성: 정상(train/good) + 불량(test/color, crack, contamination, faulty_imprint, scratch, combined, pill_type)
  - 훈련: 정상 이미지만 사용 (비지도 학습)
  - 테스트: 정상 + 7종 불량 이미지

> 데이터셋 용량이 크므로 GitHub에 포함하지 않았습니다. 위 링크에서 직접 다운로드 후 `pill/pill/` 경로에 배치해 주세요.

---

## 📈 분석 내용

### 1. 데이터 전처리 및 EDA
- 정상 / 불량 이미지 샘플 비교 시각화
- 이미지 리사이즈 및 그레이스케일 / RGB 변환

### 2. 특징 추출
| 방법 | 설명 |
|------|------|
| **Pixel** | 원본 픽셀 벡터 직접 사용 |
| **HOG** | Histogram of Oriented Gradients — 엣지 방향성 특징 |
| **HOG + HSV** | HOG에 HSV 색상 히스토그램 결합 |

### 3. 모델별 이상 탐지

#### PCA 재구성 오차 기반
- 정상 이미지로 PCA 학습 → 재구성 오차가 높으면 불량으로 판정
- 최적 주성분 수(n_components) 탐색

#### Isolation Forest
- 정상 특징 벡터로 학습 → 이상 스코어로 불량 판정
- `contamination`, `n_estimators` 파라미터 튜닝

#### PCA + Isolation Forest 결합
- PCA 차원 축소 후 Isolation Forest 적용
- 특징별(HOG, HOG+HSV) 성능 비교

### 4. 성능 평가
- Confusion Matrix, Precision, Recall, F1 Score
- 불량 유형별 Recall 히트맵으로 탐지 취약 유형 분석
- 임계값 변화에 따른 성능 곡선 분석
- TP / FP 케이스 이미지 시각화

---

## 🛠 사용 기술

- **Python**
- **NumPy / Pandas**
- **OpenCV** — 이미지 전처리, HOG, HSV 추출
- **scikit-learn** — PCA, Isolation Forest, 평가 지표
- **Matplotlib / Seaborn** — 시각화
