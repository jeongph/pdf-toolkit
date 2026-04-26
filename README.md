# pdf-toolkit

> 범용 PDF 수정 도구 — 페이지 회전·삭제·순서변경·추출, PDF 병합·분할, 메타데이터 편집을 안전한 비파괴 방식으로 수행합니다.

PyMuPDF 기반으로 일반인이 쓰는 PDF 작업의 90%를 cover하는 Claude Code 플러그인입니다. 자연어로 호출하거나 슬래시 명령으로 정밀 제어할 수 있고, **원본은 항상 보존**됩니다.

## 설치

마켓플레이스 등록(최초 1회):

```
/plugin marketplace add jeongph/claude-plugins
```

플러그인 설치:

```
/plugin install pdf-toolkit@jeongph-claude-plugins
```

## 사용 예

자연어:
```
이 PDF 54페이지 회전시켜줘
1, 2 페이지 삭제해줘
book1.pdf와 book2.pdf 합쳐줘
book.pdf를 1-100, 101-200으로 나눠줘
```

슬래시 명령:
```
/pdf-rotate book.pdf 54 180
/pdf-delete book.pdf 1,2,28
/pdf-extract book.pdf 100-200 -o samples.pdf
/pdf-merge cover.pdf body.pdf -o full.pdf
/pdf-split book.pdf 1-100,101-200,201-end
/pdf-reorder book.pdf swap:54,55
/pdf-meta book.pdf --title "..." --author "..."
```

## 지원 작업

| 작업 | slash command | 설명 |
|---|---|---|
| 페이지 회전 | `/pdf-rotate` | 단일/범위/전체 페이지 90·180·270° 회전 |
| 페이지 삭제 | `/pdf-delete` | 지정 페이지 제거 |
| 페이지 순서 변경 | `/pdf-reorder` | 새 순서 명시 또는 두 페이지 swap |
| 페이지 추출 | `/pdf-extract` | 지정 페이지만 새 PDF로 |
| PDF 병합 | `/pdf-merge` | 여러 PDF를 하나로 |
| PDF 분할 | `/pdf-split` | 페이지 범위로 여러 PDF로 분할 |
| 메타데이터 편집 | `/pdf-meta` | title·author·subject·keywords 표시·편집 |

## 페이지 지정 문법

- 단일: `5`
- 범위: `5-10`
- 다중: `1,3,5,10-12`
- 전체: `all`
- 끝까지: `15-` 또는 `15-end`

## 안전 원칙

| 원칙 | 구현 |
|---|---|
| 원본 절대 보존 | 모든 작업은 새 파일에 출력 |
| 출력 경로 명시 | `-o`로 지정. 미지정 시 `<원본>.modified.pdf` 자동 생성 |
| in-place 명시적 | `--in-place` 옵션이 있어야만 원본 덮어쓰기 |
| 검증 후 실행 | 페이지 인자·순서 등을 사전 검증, 잘못된 입력은 거부 |

## 의존성

- Python 3.8+
- [PyMuPDF](https://pymupdf.readthedocs.io/) (`pip install pymupdf`)

## 디렉토리 구조

```
pdf-toolkit/
├── .claude-plugin/plugin.json
├── skills/pdf-toolkit/
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── _util.py
│   │   ├── rotate.py
│   │   ├── delete.py
│   │   ├── reorder.py
│   │   ├── extract.py
│   │   ├── merge.py
│   │   ├── split.py
│   │   └── meta.py
│   └── references/
│       ├── safety.md
│       └── examples.md
├── commands/
│   ├── pdf-rotate.md
│   ├── pdf-delete.md
│   ├── pdf-reorder.md
│   ├── pdf-extract.md
│   ├── pdf-merge.md
│   ├── pdf-split.md
│   └── pdf-meta.md
├── requirements.txt
└── README.md
```

## 향후 확장 (v0.2.0+)

- 페이지 크기 정규화·마진 크롭
- DPI 다운샘플·이미지 재압축·워터마크
- OCR 레이어 재생성 (별도 plugin 가능성)

## 라이선스

MIT
