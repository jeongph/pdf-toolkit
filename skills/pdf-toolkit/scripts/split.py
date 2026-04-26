#!/usr/bin/env python3
"""PDF를 페이지 범위별로 여러 파일로 분할."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import require_pdf  # noqa: E402

import fitz  # noqa: E402


def parse_ranges(spec: str, n: int) -> list[tuple[int, int]]:
    """예: '1-100,101-200,201-end' -> [(1,100), (101,200), (201,n)]"""
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" not in part:
            sys.exit(f"invalid range '{part}'. expected like 1-100")
        a, b = part.split("-", 1)
        a = int(a)
        b = int(b) if b and b.lower() != "end" else n
        if a > b:
            sys.exit(f"invalid range {a}-{b}")
        out.append((a, b))
    return out


def main():
    ap = argparse.ArgumentParser(description="PDF 분할")
    ap.add_argument("pdf")
    ap.add_argument("ranges", help="페이지 범위 (예: '1-100,101-200,201-end')")
    ap.add_argument("--out-prefix", help="출력 파일명 프리픽스 (기본: 입력 파일명)")
    args = ap.parse_args()

    require_pdf(args.pdf)
    src = fitz.open(args.pdf)
    n = len(src)
    ranges = parse_ranges(args.ranges, n)
    base = args.out_prefix or os.path.splitext(args.pdf)[0]

    outs = []
    for i, (a, b) in enumerate(ranges, 1):
        sub = fitz.open()
        sub.insert_pdf(src, from_page=a - 1, to_page=b - 1)
        out_path = f"{base}.part{i:02d}.pdf"
        sub.save(out_path)
        sub.close()
        outs.append((out_path, a, b))
    src.close()

    print(f"split into {len(outs)} files:")
    for path, a, b in outs:
        print(f"  {path}: pages {a}-{b} ({b - a + 1}p)")


if __name__ == "__main__":
    main()
