"""공통 유틸: 페이지 인자 파싱, 출력 경로 결정, 안전 저장."""

import os
import sys


def parse_pages(spec: str, n: int) -> list[int]:
    """1-based 페이지 인자 파싱.

    예: 'all', '1,3,5', '5-10', '15-' (15부터 끝까지), '1,3,5-10'
    """
    s = spec.strip()
    if s.lower() == "all":
        return list(range(1, n + 1))
    pages = set()
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            a = int(a)
            b = int(b) if b and b.lower() != "end" else n
            pages.update(range(a, b + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= n)


def resolve_output(input_path: str, out_arg: str | None, in_place: bool, suffix: str = ".modified") -> str:
    if out_arg:
        return out_arg
    if in_place:
        return input_path
    base, ext = os.path.splitext(input_path)
    return f"{base}{suffix}{ext}"


def safe_save(doc, input_path: str, output_path: str) -> None:
    """입력==출력이면 incremental save, 아니면 일반 save."""
    if os.path.abspath(input_path) == os.path.abspath(output_path):
        doc.saveIncr()
    else:
        doc.save(output_path)


def require_pdf(path: str) -> None:
    if not os.path.exists(path):
        sys.exit(f"PDF not found: {path}")
    if not path.lower().endswith(".pdf"):
        print(f"warning: {path} does not end with .pdf", file=sys.stderr)
