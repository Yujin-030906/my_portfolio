# NLP_project — 타로 하루 플래너 LLM 프롬프트 설계

타로 카드 3장을 뽑아 오늘의 운세·할 일 조언·저녁 회고를 LLM으로 생성하는 하루 플래닝 서비스입니다. 팀 프로젝트에서 **데이터 설계 및 프롬프트 엔지니어링**을 담당했으며, temperature 실험을 통해 최적 생성 파라미터를 검증했습니다.

---

## 📂 파일 구성

| 파일 | 내용 |
|------|------|
| `cards_original.json` | 메이저 아르카나 22장 정방향 데이터 — 이름·영문명·키워드·의미·에너지 |
| `cards_reversed.json` | 메이저 아르카나 22장 역방향 데이터 |
| `prompts.py` | 운세·조언·회고 3종 System+User 프롬프트 템플릿 (팀 통합 버전) |
| `prompt.py` | 프롬프트 3종 독자 구현 + temperature 실험 (0.3 / 0.7 / 1.0) + CSV 결과 저장 |

> 팀 전체 코드(LLM 파이프라인, NLP 모델, FastAPI UI): [KDT12_NLP_Project](https://github.com/KDT12-NLP-Project/KDT12_NLP_Project)

---

## 👥 팀 구성 및 역할

| 팀원 | 역할 | 담당 파일 |
|------|------|---------|
| **정유진 (본인)** | 데이터 & 프롬프트 설계 | cards_original.json, cards_reversed.json, prompts.py |
| 박원호 | LLM 파이프라인 | llm_handler.py, llm_handler_gemini.py |
| 이현아 | NLP 모델 | nlp_handler.py (KeyBERT + DistilBERT + Okt) |
| 문종필 | UI & 발표 | FastAPI routers, Nest.js UI |

---

## 📈 담당 내용

### 1. 타로 카드 데이터 설계 (`cards_original.json`, `cards_reversed.json`)

메이저 아르카나 22장의 정방향·역방향 의미를 한국어로 정리한 JSON 데이터셋 직접 작성

```json
{
  "id": 0,
  "name": "바보",
  "english": "The Fool",
  "keywords": ["새로운 시작", "자유", "모험", "순수함"],
  "meaning": "새로운 출발점에 서 있습니다. 두려움 없이 첫걸음을 내딛을 때입니다.",
  "energy": "활기참"
}
```

- 정방향: 22장 (`cards_original.json`)
- 역방향: 22장 (`cards_reversed.json`)
- 각 카드: id, name, english, keywords(4개), meaning, energy 6개 필드

### 2. 프롬프트 엔지니어링 (`prompts.py`)

서비스 흐름에 맞는 3종 프롬프트 템플릿 설계

| 프롬프트 | 입력 | 출력 |
|---------|------|------|
| `FORTUNE_SYSTEM/USER` | 카드 3장 + NLP 키워드·감성 결과 | 과거-현재-미래 흐름 운세 (4~5문장) + 한 줄 요약 |
| `ADVICE_SYSTEM/USER` | 카드 3장 + 컨디션 + 할 일 | 할 일 기반 구체적 조언 (4~5문장) + 한 줄 요약 |
| `RETROSPECTIVE_SYSTEM/USER` | 카드 3장 + 완료·미완료 할 일 | 하루 총평 + 내일을 위한 한마디 (4~5문장) |

- NLP 전처리 결과(키워드, 감성 점수)를 프롬프트에 주입해 LLM 생성 품질 향상
- 출력 형식(한 줄 요약 + 본문)을 고정해 UI 파싱 용이성 확보

### 3. Temperature 실험 (`prompt.py`)

동일한 카드·컨디션·할 일 조건에서 temperature 값을 달리해 LLM 응답 특성 비교

| temperature | 특성 |
|-------------|------|
| 0.3 | 일관성 높음, 창의성 낮음 — 비슷한 표현 반복 |
| **0.7** | **균형 — 적절한 다양성과 일관성 (최종 채택)** |
| 1.0 | 창의성 높음, 일관성 낮음 — 해석이 다양하지만 산발적 |

- 실험 결과를 CSV 파일로 자동 저장 (`experiment_result_YYYYMMDD_HHMMSS.csv`)
- 카드 랜덤 뽑기: 정방향·역방향 각 50% 확률 적용

---

## 🛠 사용 기술

- **Python**
- **OpenAI GPT-4o-mini** (GitHub Models API)
- **python-dotenv** — API 키 환경변수 관리
