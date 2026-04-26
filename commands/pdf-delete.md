---
description: PDF 페이지 삭제
argument-hint: <pdf> <pages> [-o <out>]
---

# /pdf-delete

지정한 페이지를 제거합니다. 원본은 보존됩니다.

## 사용 예

```
/pdf-delete book.pdf 1
/pdf-delete book.pdf 1,2,3,612
/pdf-delete book.pdf 600-612 -o trimmed.pdf
```

## 인자

- `<pdf>` — 입력 PDF
- `<pages>` — 삭제할 페이지 인자
- `-o, --out <path>` — 출력 경로 (선택)
- `--in-place` — 원본 덮어쓰기 (선택)

## 안전 정책

5페이지 이상 삭제 시 사용자에게 한 번 더 확인하는 것이 권장됩니다 (skill이 처리).
