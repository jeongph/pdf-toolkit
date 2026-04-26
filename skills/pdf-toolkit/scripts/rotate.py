#!/usr/bin/env python3
"""지정 페이지 회전 (rotation 메타 변경)."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import parse_pages, require_pdf, resolve_output, safe_save  # noqa: E402

import fitz  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="PDF 페이지 회전")
    ap.add_argument("pdf")
    ap.add_argument("pages", help="페이지 인자 (예: 5, 5-10, 1,3,5, all)")
    ap.add_argument("degrees", type=int, choices=[90, 180, 270, -90, -180, -270])
    ap.add_argument("-o", "--out")
    ap.add_argument("--in-place", action="store_true")
    args = ap.parse_args()

    require_pdf(args.pdf)
    out = resolve_output(args.pdf, args.out, args.in_place)

    doc = fitz.open(args.pdf)
    n = len(doc)
    pages = parse_pages(args.pages, n)
    if not pages:
        sys.exit("no pages selected")

    for p in pages:
        page = doc[p - 1]
        page.set_rotation((page.rotation + args.degrees) % 360)

    safe_save(doc, args.pdf, out)
    doc.close()

    print(f"rotated {len(pages)} pages by {args.degrees}° (page list: {pages[:10]}{'...' if len(pages) > 10 else ''})")
    print(f"output: {out}")


if __name__ == "__main__":
    main()
