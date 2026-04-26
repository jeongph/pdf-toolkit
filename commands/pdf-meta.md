---
description: PDF 메타데이터 표시 또는 편집
argument-hint: <pdf> [--show | --title <t> --author <a> ...]
---

# /pdf-meta

PDF의 메타데이터(`title`, `author`, `subject`, `keywords`, `creator`, `producer`)를 표시하거나 편집합니다.

## 사용 예

```
# 현재 메타데이터 출력
/pdf-meta book.pdf --show

# 제목·저자 변경
/pdf-meta book.pdf --title "데이터 중심 애플리케이션 설계" --author "Martin Kleppmann"

# subject·keywords 추가
/pdf-meta book.pdf --subject "데이터베이스" --keywords "DDIA, 분산시스템"
```

## 인자

- `<pdf>` — 입력 PDF
- `--show` — 현재 메타데이터를 JSON으로 출력 후 종료
- `--title`, `--author`, `--subject`, `--keywords`, `--creator`, `--producer` — 편집할 필드 (선택, 여러 개 동시 가능)
- `-o, --out <path>` — 출력 경로 (선택)
- `--in-place` — 원본 덮어쓰기 (선택)
