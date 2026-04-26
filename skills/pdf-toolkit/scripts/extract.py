#!/usr/bin/env python3
"""지정 페이지를 새 PDF로 추출."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import parse_pages, require_pdf  # noqa: E402

import fitz  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="PDF 페이지 추출")
    ap.add_argument("pdf")
    ap.add_argument("pages", help="추출할 페이지 (예: 1-50, 100-200)")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    require_pdf(args.pdf)
    out = args.out or f"{os.path.splitext(args.pdf)[0]}.extracted.pdf"

    src = fitz.open(args.pdf)
    n = len(src)
    pages = parse_pages(args.pages, n)
    if not pages:
        sys.exit("no pages to extract")

    dst = fitz.open()
    for p in pages:
        dst.insert_pdf(src, from_page=p - 1, to_page=p - 1)

    dst.save(out)
    dst.close()
    src.close()

    print(f"extracted {len(pages)} pages from {n}-page PDF -> {out}")


if __name__ == "__main__":
    main()
