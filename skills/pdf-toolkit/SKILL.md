---
name: pdf-toolkit
description: Use this skill when the user wants to modify PDF files — rotate pages, delete pages, reorder pages, extract pages into new PDF, merge multiple PDFs, split a PDF, or edit PDF metadata. Korean triggers "PDF 회전", "페이지 회전", "페이지 회전시켜", "페이지 삭제", "페이지 빼", "페이지 제거", "PDF 합치기", "PDF 병합", "PDF 분할", "PDF 나누기", "페이지 추출", "페이지 뽑아", "페이지 순서", "PDF 순서 바꿔", "PDF 메타데이터", "제목 바꿔", "PDF 수정". English triggers "rotate PDF page", "delete page", "merge PDFs", "split PDF", "extract pages", "reorder pages", "edit PDF metadata". Non-destructive by default: original file is preserved, output goes to new file unless user explicitly requests in-place edit.
---

# PDF Toolkit

PyMuPDF 기반 범용 PDF 수정 도구. 페이지·문서·메타데이터 수정을 안전한 비파괴 방식으로 처리합니다.

## 안전 원칙 (필수 준수)

1. **원본 절대 보존** — 모든 작업은 새 파일에 출력. 사용자가 명시적으로 `--in-place` 요청한 경우에만 덮어씀
2. **출력 경로** — `-o`로 명시. 미지정 시 `<원본>.modified.pdf` 자동 생성
3. **사전 확인** — 5페이지 이상 삭제·전체 순서 대규모 변경 시 `AskUserQuestion`으로 재확인
4. **백업 권장** — 첫 작업 시 사용자에게 "원본은 자동 보존됩니다"라고 안내

## 지원 작업

| 작업 | 스크립트 | slash command | 설명 |
|---|---|---|---|
| 페이지 회전 | `rotate.py` | `/pdf-rotate` | 단일/범위/전체 페이지 90·180·270° 회전 |
| 페이지 삭제 | `delete.py` | `/pdf-delete` | 지정 페이지 제거 |
| 페이지 순서 변경 | `reorder.py` | `/pdf-reorder` | 새 순서 명시 또는 swap |
| 페이지 추출 | `extract.py` | `/pdf-extract` | 지정 페이지만 새 PDF로 |
| PDF 병합 | `merge.py` | `/pdf-merge` | 여러 PDF를 하나로 |
| PDF 분할 | `split.py` | `/pdf-split` | 페이지 범위로 여러 PDF로 분할 |
| 메타데이터 편집 | `meta.py` | `/pdf-meta` | title·author·subject·keywords 편집 |

## 페이지 지정 문법

모든 페이지 인자는 다음 문법을 따른다 (1-based):
- 단일: `5`
- 범위: `5-10`
- 다중: `1,3,5,10-12`
- 전체: `all`
- 끝까지: `5-` (5페이지부터 마지막까지)

## 워크플로우

### 1. 입력 검증
- PDF 경로가 실제 존재하는지 확인
- 페이지 인자가 PDF 페이지 범위 안에 있는지 검증
- 출력 경로가 입력 경로와 같으면 `--in-place` 명시 여부 확인

### 2. 의존성 점검
```bash
python3 -c "import fitz" 2>&1
```
- 없으면 `pip install pymupdf` 안내

### 3. 작업 실행
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/pdf-toolkit/scripts/<task>.py <args> -o <out>
```

### 4. 결과 보고
- 입력·출력 파일 경로
- 작업 요약 (예: "p.5 180° 회전, p.7-9 삭제 → 총 612 → 609페이지")
- 변경 전후 페이지 수

### 5. 후속 동작 안내 (해당 시)
- 결과 PDF 검사가 필요하면 `pdf-scan-audit`으로 연결 안내

## 자연어 명령 처리

사용자가 자연어로 "이 PDF 54페이지 회전시켜줘"라고 하면:
1. 의도 파악: 작업=rotate, 페이지=54, 각도=180 (기본값) — 각도 생략 시 사용자에게 확인
2. 위 워크플로우 진행
3. 출력 경로 미명시 시 자동 생성

## 자세한 가이드

- 안전 원칙 상세: `references/safety.md`
- 자주 쓰는 작업 레시피: `references/examples.md`
