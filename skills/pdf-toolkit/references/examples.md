# 자주 쓰는 작업 레시피

## 스캔본 후처리

### 회전 잘못된 페이지 한 개 고치기
```bash
/pdf-rotate book.pdf 54 180
```

### 표지·뒷표지 제외하고 본문만 추출
```bash
/pdf-extract book.pdf 5-610 -o body-only.pdf
```

### 빈 페이지 여러 개 한꺼번에 삭제
```bash
/pdf-delete book.pdf 2,28,57,143,288 -o cleaned.pdf
```

### 페이지 순서가 뒤바뀐 경우 (54와 55가 서로 바뀜)
```bash
/pdf-reorder book.pdf swap:54,55
```

## 책 분할·합본

### 한 권을 여러 권으로 분할
```bash
/pdf-split book.pdf 1-200,201-400,401-end
```

### 여러 챕터를 한 권으로 합치기
```bash
/pdf-merge ch01.pdf ch02.pdf ch03.pdf -o full.pdf
```

## 메타데이터 정리

### 스캐너가 남긴 빈 메타 채우기
```bash
/pdf-meta book.pdf \
  --title "데이터 중심 애플리케이션 설계" \
  --author "Martin Kleppmann" \
  --subject "Distributed Systems"
```

## 전체 페이지 90° 회전 (가로 스캔본을 세로로)
```bash
/pdf-rotate scan.pdf all 90
```
