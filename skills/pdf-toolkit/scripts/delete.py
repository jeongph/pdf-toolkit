#!/usr/bin/env python3
"""지정 페이지 삭제."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import parse_pages, require_pdf, resolve_output, safe_save  # noqa: E402

import fitz  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="PDF 페이지 삭제")
    ap.add_argument("pdf")
    ap.add_argument("pages", help="삭제할 페이지 (예: 5, 5-10, 1,3,5)")
    ap.add_argument("-o", "--out")
    ap.add_argument("--in-place", action="store_true")
    args = ap.parse_args()

    require_pdf(args.pdf)
    out = resolve_output(args.pdf, args.out, args.in_place)

    doc = fitz.open(args.pdf)
    n_before = len(doc)
    pages = parse_pages(args.pages, n_before)
    if not pages:
        sys.exit("no pages to delete")

    for p in sorted(pages, reverse=True):
        doc.delete_page(p - 1)

    n_after = len(doc)
    safe_save(doc, args.pdf, out)
    doc.close()

    print(f"deleted {len(pages)} pages: {pages[:10]}{'...' if len(pages) > 10 else ''}")
    print(f"pages: {n_before} -> {n_after}")
    print(f"output: {out}")


if __name__ == "__main__":
    main()
