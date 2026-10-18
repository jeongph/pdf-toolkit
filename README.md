# pdf-toolkit

[![version](https://img.shields.io/github/v/release/jeongph/pdf-toolkit?label=version&color=blue)](https://github.com/jeongph/pdf-toolkit/releases)
[![license](https://img.shields.io/github/license/jeongph/pdf-toolkit?color=lightgrey)](LICENSE)

PDF 페이지를 회전하거나 삭제하고, 문서를 합치거나 나눕니다. 기본적으로 원본은 그대로 둡니다.

결과는 새 파일에 저장합니다. 원본을 덮어쓰려면 `--in-place` 옵션을 명시해야 합니다.

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

| 작업 | 슬래시 명령 | 설명 |
|---|---|---|
| 페이지 회전 | `/pdf-rotate` | 단일/범위/전체 페이지 90·180·270° 회전 |
| 페이지 삭제 | `/pdf-delete` | 지정 페이지 제거 |
| 페이지 순서 변경 | `/pdf-reorder` | 새 순서 명시 또는 두 페이지 교환 |
| 페이지 추출 | `/pdf-extract` | 지정 페이지만 새 PDF로 |
| PDF 병합 | `/pdf-merge` | 여러 PDF를 하나로 |
| PDF 분할 | `/pdf-split` | 페이지 범위로 여러 PDF로 분할 |
| 메타데이터 편집 | `/pdf-meta` | title, author, subject, keywords 표시와 편집 |

## 페이지 지정 문법

- 단일: `5`
- 범위: `5-10`
- 다중: `1,3,5,10-12`
- 전체: `all`
- 끝까지: `15-` 또는 `15-end`

## 안전 원칙

| 원칙 | 구현 |
|---|---|
| 원본 보존이 기본 | 기본적으로 결과를 새 파일에 출력 |
| 출력 경로 명시 | `-o`로 지정. 미지정 시 `<원본>.modified.pdf` 자동 생성 |
| 원본 덮어쓰기 조건 | `--in-place` 옵션이 있어야만 원본 덮어쓰기 |
| 검증 후 실행 | 페이지 인자, 순서 등을 사전 검증하고 잘못된 입력은 거부 |

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

- 페이지 크기 정규화, 마진 크롭
- DPI 다운샘플, 이미지 재압축, 워터마크
- OCR 레이어 재생성 (별도 플러그인으로 제공할 가능성)

## 라이선스

MIT
