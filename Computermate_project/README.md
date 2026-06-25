# Computermate_project — Anomalib 기반 볼트 불량 이상 탐지

Anomalib 라이브러리를 활용해 PatchCore·EfficientAD 모델로 볼트(Bolt) 이미지의 불량 여부를 비지도 학습 기반으로 탐지하는 프로젝트입니다.

---

## 📂 파일 구성

| 파일 | 내용 |
|------|------|
| `Anomalib_Studio/anomalib_readme.ipynb` | PatchCore 모델로 MVTecAD 데이터셋 이상 탐지 기본 실습 |
| `Anomalib_EfficientAD/01_getting started.ipynb` | Anomalib 환경 설정 및 시작 가이드 |
| `Anomalib_EfficientAD/02_folder.ipynb` | 커스텀 폴더 데이터셋(Folder) 구성 실습 |
| `Anomalib_EfficientAD/03_02~03_09.ipynb` | 단계별 EfficientAD 실험 노트북 |
| `Anomalib_EfficientAD/03_EfficientAD.ipynb` | EfficientAD 전체 파이프라인 — 학습·추론·이상 맵 시각화·평가 |

---

## 📈 분석 내용

### 1. PatchCore — MVTecAD 기반 이상 탐지 (`anomalib_readme.ipynb`)

Anomalib 공식 API 기반으로 PatchCore 모델을 MVTecAD 데이터셋에 적용

```python
from anomalib.data import MVTecAD
from anomalib.models import Patchcore
from anomalib.engine import Engine

datamodule = MVTecAD()
model = Patchcore()
engine = Engine()
engine.fit(datamodule=datamodule, model=model)
```

### 2. EfficientAD — 볼트 불량 탐지 (`03_EfficientAD.ipynb`)

실제 촬영한 볼트 OK/NG 이미지로 EfficientAD 모델 전이 적용

**데이터 구성**
- `train/good` — 정상 볼트 이미지 (학습용)
- `test/ng` — 불량 볼트 이미지 (테스트용)

**학습 파이프라인**

```python
model = EfficientAd(
    imagenet_dir='./datasets/imagenette',
    teacher_out_channels=384,
    model_size='small',
    lr=0.0001,
    weight_decay=1e-05,
)

engine = Engine(
    accelerator="gpu",
    max_epochs=50,
    callbacks=[ModelCheckpoint(...), EarlyStopping(patience=5)],
)
engine.fit(datamodule=folder_datamodule, model=model)
```

**Threshold 산출 — train/good 95 Percentile**

```python
train_preds = engine.predict(model=model, data_path=dataset_root / "train" / "good")
train_scores = [float(p.pred_score[0].item()) for p in train_preds]
threshold = np.percentile(train_scores, 95)
```

- 테스트 데이터를 전혀 사용하지 않고 정상 이미지 점수 분포에서만 임계값 결정
- Anomaly Map, Heat Map, Predicted Mask 시각화

**평가 지표**
- Confusion Matrix
- Precision / Recall / F1-score
- AUROC / Average Precision (AP)

---

## 🛠 사용 기술

- **Python**
- **Anomalib** — PatchCore, EfficientAD 이상 탐지 프레임워크
- **PyTorch Lightning** — Engine, Callbacks
- **scikit-learn** — Confusion Matrix, Precision/Recall/F1/AUROC
- **Matplotlib / PIL** — 이상 맵 시각화
