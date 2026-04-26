#!/usr/bin/env python3
"""페이지 순서 변경."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _util import require_pdf, resolve_output, safe_save  # noqa: E402

import fitz  # noqa: E402


def parse_order(spec: str, n: int) -> list[int]:
    """0-based 인덱스 시퀀스 반환.

    예:
      'swap:5,7'              -> 5번과 7번 페이지만 교환
      '3,1,2,4-end'           -> 새 순서 명시 (모든 페이지 정확히 한 번)
    """
    s = spec.strip()
    if s.startswith("swap:"):
        a, b = (int(x) for x in s[5:].split(","))
        order = list(range(n))
        order[a - 1], order[b - 1] = order[b - 1], order[a - 1]
        return order

    out = []
    for part in s.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            a = int(a)
            b = int(b) if b and b.lower() != "end" else n
            out.extend(range(a - 1, b))
        else:
            out.append(int(part) - 1)
    return out


def main():
    ap = argparse.ArgumentParser(description="PDF 페이지 순서 변경")
    ap.add_argument("pdf")
    ap.add_argument(
        "order",
        help="새 순서 (예: '3,1,2,4-end') 또는 'swap:5,7'",
    )
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    require_pdf(args.pdf)
    out = resolve_output(args.pdf, args.out, False, suffix=".reordered")

    doc = fitz.open(args.pdf)
    n = len(doc)
    new_order = parse_order(args.order, n)

    if sorted(new_order) != list(range(n)):
        sys.exit(
            f"order spec must reference all {n} pages exactly once. "
            f"Got {len(new_order)} entries; missing or duplicates present."
        )

    doc.select(new_order)
    safe_save(doc, args.pdf, out)
    doc.close()

    print(f"reordered {n} pages -> {out}")


if __name__ == "__main__":
    main()
