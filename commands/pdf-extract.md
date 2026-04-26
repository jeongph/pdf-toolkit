---
description: PDF에서 지정 페이지만 새 파일로 추출
argument-hint: <pdf> <pages> [-o <out>]
---

# /pdf-extract

지정한 페이지만 모아 **새 PDF로 출력**합니다. 원본은 변경되지 않습니다.

## 사용 예

```
/pdf-extract book.pdf 1-50 -o intro.pdf
/pdf-extract book.pdf 100,200,300 -o samples.pdf
/pdf-extract book.pdf 600-end -o appendix.pdf
```

## 인자

- `<pdf>` — 입력 PDF
- `<pages>` — 추출할 페이지 인자
- `-o, --out <path>` — 출력 경로 (선택, 기본 `<원본>.extracted.pdf`)
