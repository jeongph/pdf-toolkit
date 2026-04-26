---
description: 여러 PDF를 하나로 병합
argument-hint: <pdf1> <pdf2> [<pdf3>...] -o <out>
---

# /pdf-merge

두 개 이상의 PDF를 인자 순서대로 병합해 새 파일에 출력합니다.

## 사용 예

```
/pdf-merge cover.pdf body.pdf appendix.pdf -o full.pdf
/pdf-merge ch01.pdf ch02.pdf ch03.pdf -o book.pdf
```

## 인자

- `<pdfs...>` — 병합할 PDF 두 개 이상 (인자 순서대로 결합)
- `-o, --out <path>` — 출력 경로 (필수)
