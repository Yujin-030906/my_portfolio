# Deeplearning_project — PCB 불량 검출 YOLOv8 전이학습

PCB(인쇄회로기판) 이미지에서 6종 불량을 탐지하는 객체 검출 프로젝트입니다. Pascal VOC XML 형식의 어노테이션을 YOLO 포맷으로 변환한 뒤 YOLOv8s 전이학습을 적용하고, 클래스별 AP 분석 및 추론 데모까지 구현하였습니다.

---

## 📂 파일 구성

| 파일 | 내용 |
|------|------|
| `project2.ipynb` | 데이터 EDA · 클래스 분포 · 바운딩 박스 면적 분석 |
| `project3.ipynb` | Pascal VOC XML → YOLO 포맷 변환 · Train/Val/Test 분할 · dataset.yaml 생성 |
| `project4.ipynb` | YOLOv8s 전이학습 · 하이퍼파라미터 설정 · 학습 곡선 시각화 |
| `project5.ipynb` | Test set 평가 · 클래스별 AP 분석 · FP/FN 오탐지 시각화 |
| `project6.ipynb` | 단일 이미지 추론 · 배치 추론 · 추론 속도 벤치마크 |
| `eda_class_distribution.png` | 클래스별 인스턴스 수 분포 막대 그래프 |
| `eda_bbox_area.png` | 바운딩 박스 면적 분포 히스토그램 |
| `eval_class_ap.png` | 클래스별 AP@0.5 비교 막대 그래프 |
| `inference_single.png` | 단일 이미지 추론 결과 시각화 |
| `inference_speed.png` | 추론 속도 벤치마크 결과 |

---

## 📊 데이터 소스

- **PCB Defects Dataset** (Pascal VOC XML 어노테이션)
  - 불량 클래스 6종: `missing_hole`, `mouse_bite`, `open_circuit`, `short`, `spur`, `spurious_copper`
  - 어노테이션 형식: Pascal VOC XML → YOLO `.txt` 변환 후 사용
  - 분할: Train / Val / Test (Test 70장)

> 데이터셋 용량이 크므로 GitHub에 포함하지 않았습니다. PCB Defects Dataset을 직접 다운로드 후 `pcb-defects/` 경로에 배치해 주세요.

---

## 📈 분석 내용

### 1. EDA (project2)
- 클래스별 인스턴스 수 분포 확인
- 바운딩 박스 면적 분포 분석 (클래스 간 크기 불균형 파악)
- 샘플 이미지 및 어노테이션 시각화

### 2. 데이터 전처리 (project3)
- Pascal VOC XML → YOLO 정규화 좌표 변환 (`voc_to_yolo()`)
- 이미지-어노테이션 쌍 수집 및 Train / Val / Test 랜덤 분할
- YOLOv8 학습용 `dataset.yaml` 자동 생성

### 3. 모델 학습 (project4)
- **베이스 모델**: YOLOv8s (`yolov8s.pt`, COCO 사전학습 가중치)
- **주요 하이퍼파라미터**

| 파라미터 | 값 |
|---------|-----|
| epochs | 100 |
| imgsz | 640 |
| batch | 16 |
| lr0 | 0.01 |
| optimizer | SGD |
| warmup_epochs | 3 |

- 학습 곡선(box loss, cls loss, mAP) 시각화

### 4. 모델 평가 (project5)

**Test Set 최종 성능**

| 지표 | 값 |
|------|-----|
| mAP@0.5 | **0.4188** |
| mAP@0.5:0.95 | 0.1381 |
| Precision | 0.6088 |
| Recall | 0.2414 |

**클래스별 AP@0.5**

| 클래스 | AP@0.5 |
|--------|--------|
| missing_hole | 0.431 |
| mouse_bite | 0.342 |
| open_circuit | 0.263 |
| short | 0.522 |
| spur | **0.572** |
| spurious_copper | 0.383 |

- FP(오탐지) / FN(미탐지) 케이스 이미지 시각화

### 5. 추론 데모 (project6)
- 단일 이미지 추론 및 바운딩 박스 시각화
- 배치 추론 (다중 이미지 일괄 처리)
- 추론 속도 벤치마크 (preprocessing / inference / postprocessing 단계별 측정)
