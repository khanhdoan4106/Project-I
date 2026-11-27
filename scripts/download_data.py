"""Tải bộ dữ liệu Facebook của SNAP, giải nén và kiểm tra lại.

Cách chạy (từ thư mục gốc của repo):
    python scripts/download_data.py          # đã có file .gz thì không tải lại
    python scripts/download_data.py --force  # tải lại từ đầu
"""

import argparse
import gzip
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from sna.io import read_edge_list  # noqa: E402

URL = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
RAW_FILE = ROOT / "data" / "raw" / "facebook_combined.txt.gz"
OUT_FILE = ROOT / "data" / "facebook_combined.txt"

# Số liệu SNAP công bố cho bộ dữ liệu này
EXPECTED_NODES = 4039
EXPECTED_EDGES = 88234


def download(force):
    """Tải file .gz về data/raw/, đã có thì bỏ qua (trừ khi force)."""
    if RAW_FILE.exists() and not force:
        print(f"Đã có {RAW_FILE.relative_to(ROOT)}, không tải lại (dùng --force để tải lại).")
        return
    RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    print(f"Đang tải {URL} ...")
    tmp = RAW_FILE.with_suffix(".part")
    with urllib.request.urlopen(URL, timeout=60) as resp, open(tmp, "wb") as f:
        shutil.copyfileobj(resp, f)
    tmp.replace(RAW_FILE)  # tải xong mới đổi tên, tránh để lại file hỏng
    print(f"Đã lưu {RAW_FILE.relative_to(ROOT)}")


def extract():
    """Giải nén file .gz ra data/facebook_combined.txt."""
    with gzip.open(RAW_FILE, "rb") as src, open(OUT_FILE, "wb") as dst:
        shutil.copyfileobj(src, dst)
    print(f"Đã giải nén ra {OUT_FILE.relative_to(ROOT)}")


def main():
    # In tiếng Việt không bị lỗi trên console Windows (cp1252)
    sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Tải dữ liệu Facebook của SNAP")
    parser.add_argument("--force", action="store_true", help="tải lại dù đã có file")
    args = parser.parse_args()

    try:
        download(args.force)
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"Lỗi: không tải được dữ liệu ({e}). Kiểm tra lại kết nối mạng rồi chạy lại.")
        return 1

    extract()

    _, stats = read_edge_list(OUT_FILE)
    print("Thống kê:")
    print(f"  Số dòng đọc: {stats['lines_read']}")
    for reason, count in stats["skipped"].items():
        print(f"  Bỏ qua ({reason}): {count}")
    print(f"  Số nút: {stats['nodes']}")
    print(f"  Số cạnh: {stats['edges']}")

    if stats["nodes"] != EXPECTED_NODES or stats["edges"] != EXPECTED_EDGES:
        print(f"Lỗi: cần {EXPECTED_NODES} nút và {EXPECTED_EDGES} cạnh, dữ liệu không khớp.")
        return 1
    print("Dữ liệu khớp với số liệu của SNAP.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
