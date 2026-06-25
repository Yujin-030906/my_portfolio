# MachineLearning_project — 심장질환 예측 머신러닝 모델 비교 분석

65세 이상 노인 데이터를 대상으로 Decision Tree·Logistic Regression·Random Forest·Gradient Boosting·XGBoost·LightGBM 6가지 분류 모델을 학습하고 성능을 비교한 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 내용 |
|------|------|
| `heart_disease.ipynb` | 데이터 전처리 · EDA · 모델 학습 · 성능 비교 · 하이퍼파라미터 튜닝 전체 파이프라인 |
| `train.csv` | 심장질환 예측 훈련 데이터 |
| `test.csv` | 심장질환 예측 테스트 데이터 |

---

## 📊 데이터 소스

- `train.csv` / `test.csv` — 심장질환 예측 데이터셋
  - 주요 컬럼: Age, Sex, Chest pain type, BP, Cholesterol, FBS over 120, EKG results, Max HR, Exercise angina, ST depression, Slope of ST, Number of vessels fluro, Thallium, Heart Disease

---

## 📈 분석 내용

### 1. 데이터 전처리

- `Heart Disease` 컬럼 `Presence` / `Absence` → 1 / 0 수치 변환
- 65세 이상 여부 파생 컬럼(`old`) 추가
- `id` 컬럼 제거
- 65세 이상 데이터만 추출해 `df_old` 생성

### 2. EDA

- 전체 연령 / 65세 이상 심장질환 발병 현황 countplot 비교
- 발병 비율 barplot, 나이-심장질환 boxplot
- 흉통 유형(Chest pain type)별 심장질환 발병 분포
- 변수 간 상관관계 히트맵
- 탈륨(Thallium) 값과 심장질환 관계 산점도 · countplot

### 3. 모델 학습 및 성능 비교

| 모델 | Accuracy | F1 Score | ROC-AUC |
|------|----------|----------|---------|
| Decision Tree | 0.809 | 0.837 | 0.803 |
| Logistic Regression | 0.872 | 0.891 | 0.944 |
| Random Forest | 0.869 | 0.888 | 0.939 |
| Gradient Boosting | **0.875** | **0.894** | **0.947** |
| XGBoost | 0.874 | 0.892 | 0.946 |
| LightGBM | 0.875 | 0.893 | 0.946 |

### 4. 성능 평가

- Accuracy · Precision · Recall · F1 Score · ROC-AUC 5개 지표 종합 비교
- Gradient Boosting 모델 Confusion Matrix, ROC Curve 시각화
- 전 모델 ROC Curve 비교 그래프

### 5. 하이퍼파라미터 튜닝 (GridSearchCV)

- Gradient Boosting 대상 `n_estimators`, `learning_rate`, `max_depth`, `min_samples_split` 탐색
- 최적 파라미터: `learning_rate=0.1`, `max_depth=3`, `min_samples_split=5`, `n_estimators=200`
- 튜닝 후 ROC-AUC: **0.9509**

### 6. 특성 중요도 분석

- 전 모델 공통 상위 중요 특성: **Thallium(탈륨) > Chest pain type > Max HR**
- 최종 모델(Gradient Boosting) 특성 중요도 barplot 시각화

### 7. 예측 모델

- 전체 데이터로 최종 Gradient Boosting 모델 재학습
- 가상 환자 데이터 입력 → 심장질환 여부 예측 및 발병 확률 출력

---

## 🛠 사용 기술

- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **scikit-learn** (DecisionTree, LogisticRegression, RandomForest, GradientBoosting, GridSearchCV)
- **XGBoost**
- **LightGBM**
