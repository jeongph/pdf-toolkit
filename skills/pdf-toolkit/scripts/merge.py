#!/usr/bin/env python3
"""여러 PDF를 하나로 병합."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import require_pdf  # noqa: E402

import fitz  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="여러 PDF 병합")
    ap.add_argument("pdfs", nargs="+", help="입력 PDF 두 개 이상")
    ap.add_argument("-o", "--out", required=True, help="출력 경로")
    args = ap.parse_args()

    if len(args.pdfs) < 2:
        sys.exit("at least 2 PDFs required to merge")
    for p in args.pdfs:
        require_pdf(p)

    out_doc = fitz.open()
    total_pages = 0
    parts = []
    for p in args.pdfs:
        d = fitz.open(p)
        parts.append((os.path.basename(p), len(d)))
        out_doc.insert_pdf(d)
        total_pages += len(d)
        d.close()

    out_doc.save(args.out)
    out_doc.close()

    print(f"merged {len(args.pdfs)} PDFs ({total_pages} total pages) -> {args.out}")
    for name, n in parts:
        print(f"  - {name}: {n} pages")


if __name__ == "__main__":
    main()
