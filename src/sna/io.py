"""Đọc dữ liệu đồ thị từ file."""

from .graph import Graph


def read_edge_list(path):
    """Đọc file danh sách cạnh, mỗi dòng có dạng "u v" (u, v là số nguyên).

    Các dòng bị bỏ qua:
    - blank: dòng trống
    - comment: dòng bắt đầu bằng #
    - malformed: không đúng 2 cột hoặc không phải số nguyên
    - self_loop: cạnh tự nối (u == v)
    - duplicate: cạnh đã đọc rồi (kể cả khi đảo chiều, vd "1 2" và "2 1")

    Trả về (graph, stats).
    """
    graph = Graph()
    skipped = {"blank": 0, "comment": 0, "malformed": 0, "self_loop": 0, "duplicate": 0}
    lines_read = 0

    with open(path, encoding="utf-8") as f:
        for line in f:
            lines_read += 1
            line = line.strip()
            if not line:
                skipped["blank"] += 1
                continue
            if line.startswith("#"):
                skipped["comment"] += 1
                continue

            parts = line.split()
            if len(parts) != 2:
                skipped["malformed"] += 1
                continue
            try:
                u, v = int(parts[0]), int(parts[1])
            except ValueError:
                skipped["malformed"] += 1
                continue

            if u == v:
                skipped["self_loop"] += 1
                continue
            if not graph.add_edge(u, v):
                skipped["duplicate"] += 1

    stats = {
        "lines_read": lines_read,
        "skipped": skipped,
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
    }
    return graph, stats
