---
description: PDF를 페이지 범위별로 여러 파일로 분할
argument-hint: <pdf> <ranges> [--out-prefix <prefix>]
---

# /pdf-split

PDF를 지정한 페이지 범위로 잘라 여러 파일로 분할합니다.

## 사용 예

```
/pdf-split book.pdf 1-100,101-200,201-end
/pdf-split book.pdf 1-50,51-100 --out-prefix chapters
```

## 인자

- `<pdf>` — 입력 PDF
- `<ranges>` — 콤마로 구분된 페이지 범위 (예: `1-100,101-200,201-end`)
- `--out-prefix <prefix>` — 출력 파일명 프리픽스 (기본: 입력 파일명). 출력은 `<prefix>.part01.pdf`, `<prefix>.part02.pdf`, ... 형식
