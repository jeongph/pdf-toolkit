#!/usr/bin/env python3
"""PDF 메타데이터 표시 또는 편집."""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import require_pdf, resolve_output, safe_save  # noqa: E402

import fitz  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="PDF 메타데이터 표시·편집")
    ap.add_argument("pdf")
    ap.add_argument("--show", action="store_true", help="현재 메타데이터를 JSON으로 출력하고 종료")
    ap.add_argument("--title")
    ap.add_argument("--author")
    ap.add_argument("--subject")
    ap.add_argument("--keywords")
    ap.add_argument("--creator")
    ap.add_argument("--producer")
    ap.add_argument("-o", "--out")
    ap.add_argument("--in-place", action="store_true")
    args = ap.parse_args()

    require_pdf(args.pdf)

    doc = fitz.open(args.pdf)
    if args.show:
        print(json.dumps(doc.metadata, ensure_ascii=False, indent=2))
        doc.close()
        return

    fields = {
        "title": args.title,
        "author": args.author,
        "subject": args.subject,
        "keywords": args.keywords,
        "creator": args.creator,
        "producer": args.producer,
    }
    changes = {k: v for k, v in fields.items() if v is not None}
    if not changes:
        sys.exit("no metadata fields specified. use --show to view, or pass --title/--author/etc.")

    new_meta = dict(doc.metadata or {})
    new_meta.update(changes)
    doc.set_metadata(new_meta)

    out = resolve_output(args.pdf, args.out, args.in_place)
    safe_save(doc, args.pdf, out)
    doc.close()

    print("updated fields:")
    for k, v in changes.items():
        print(f"  {k}: {v}")
    print(f"output: {out}")


if __name__ == "__main__":
    main()
