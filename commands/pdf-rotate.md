---
description: PDF 페이지 회전 (90/180/270°)
argument-hint: <pdf> <pages> <degrees> [-o <out>]
---

# /pdf-rotate

지정한 페이지를 회전시킵니다. 원본은 보존되고 결과는 `<원본>.modified.pdf`로 출력됩니다.

## 사용 예

```
/pdf-rotate book.pdf 54 180
/pdf-rotate book.pdf 54,98,140 90
/pdf-rotate book.pdf 100-200 -90
/pdf-rotate book.pdf all 180 -o flipped.pdf
```

## 인자

- `<pdf>` — 입력 PDF 경로
- `<pages>` — 페이지 인자 (예: `5`, `5-10`, `1,3,5`, `all`, `15-`)
- `<degrees>` — 회전 각도. 90, 180, 270, -90, -180, -270 중 하나
- `-o, --out <path>` — 출력 경로 (선택)
- `--in-place` — 원본 덮어쓰기 (선택, 명시 필요)

## 동작

`${CLAUDE_PLUGIN_ROOT}/skills/pdf-toolkit/scripts/rotate.py` 실행. 페이지 메타의 `/Rotate` 값만 변경하므로 빠르고 무손실입니다.
