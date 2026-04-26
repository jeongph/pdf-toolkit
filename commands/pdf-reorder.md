---
description: PDF 페이지 순서 변경 또는 두 페이지 교환
argument-hint: <pdf> <order|swap:a,b> [-o <out>]
---

# /pdf-reorder

페이지 순서를 새로 명시하거나 두 페이지만 교환합니다.

## 사용 예

```
# 두 페이지만 교환
/pdf-reorder book.pdf swap:54,55

# 새 순서 전체 명시 (모든 페이지를 정확히 한 번 참조해야 함)
/pdf-reorder book.pdf "3,1,2,4-end"

# 결과 경로 지정
/pdf-reorder book.pdf swap:54,55 -o fixed.pdf
```

## 인자

- `<pdf>` — 입력 PDF
- `<order>` — 새 순서 또는 `swap:a,b`
  - `swap:5,7`: 5번과 7번만 교환
  - `3,1,2,4-end`: 새 순서 전체 명시 (모든 페이지 정확히 한 번)
- `-o, --out <path>` — 출력 경로 (선택, 기본 `<원본>.reordered.pdf`)

## 안전 정책

새 순서가 모든 페이지를 정확히 한 번 참조하지 않으면 작업 거부.
