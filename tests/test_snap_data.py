"""Kiểm tra file dữ liệu Facebook của SNAP có sẵn trong repo (không tải mạng)."""

from pathlib import Path

from sna.io import read_edge_list

DATA = Path(__file__).resolve().parent.parent / "data" / "facebook_combined.txt"


def test_snap_facebook_data():
    _, stats = read_edge_list(DATA)

    assert stats["nodes"] == 4039
    assert stats["edges"] == 88234
    # File sạch, không có dòng nào bị bỏ qua
    assert sum(stats["skipped"].values()) == 0
