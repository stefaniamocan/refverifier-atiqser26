"""Fetch the 10 arXiv PDFs of the Stage 1 PDF-vs-LaTeX evaluation and record
their SHA-256 hashes into data/stage1_pdf/papers_manifest.csv.

Usage: python scripts/fetch_pdfs.py [target_dir]   (default: data/stage1_pdf/pdfs)
Standard library only. PDFs are NOT redistributed with this package; arXiv
serves them under each paper's own licence.
"""
import csv
import hashlib
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data/stage1_pdf/papers_manifest.csv"


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/stage1_pdf/pdfs"
    out.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
    for row in rows:
        aid = row["arxiv_id"]
        dst = out / f"{aid}.pdf"
        if not dst.exists():
            print(f"fetching {aid} ...")
            urllib.request.urlretrieve(row["pdf_url"], dst)
            time.sleep(3)  # be polite to arXiv
        digest = hashlib.sha256(dst.read_bytes()).hexdigest()
        if row["sha256_pdf"] and row["sha256_pdf"] != digest:
            print(f"HASH MISMATCH {aid}: manifest {row['sha256_pdf'][:12]}..., got {digest[:12]}...")
        row["sha256_pdf"] = digest
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("manifest updated with hashes")


if __name__ == "__main__":
    main()
