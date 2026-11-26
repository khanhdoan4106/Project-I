"""Biểu diễn đồ thị vô hướng bằng danh sách kề."""


class Graph:
    """Đồ thị vô hướng, lưu dạng dict: nút -> tập các hàng xóm."""

    def __init__(self):
        self._adj = {}

    def add_node(self, u):
        """Thêm nút u, nếu đã có thì bỏ qua."""
        if u not in self._adj:
            self._adj[u] = set()

    def add_edge(self, u, v):
        """Thêm cạnh u-v. Bỏ qua cạnh tự nối và cạnh đã có.

        Trả về True nếu cạnh được thêm mới, False nếu bị bỏ qua.
        """
        if u == v:
            return False
        self.add_node(u)
        self.add_node(v)
        if v in self._adj[u]:
            return False
        self._adj[u].add(v)
        self._adj[v].add(u)
        return True

    def has_node(self, u):
        return u in self._adj

    def has_edge(self, u, v):
        return u in self._adj and v in self._adj[u]

    def neighbors(self, u):
        """Trả về tập hàng xóm của u. Báo KeyError nếu u không có trong đồ thị."""
        if u not in self._adj:
            raise KeyError(f"Nút {u!r} không có trong đồ thị")
        return self._adj[u]

    def nodes(self):
        """Danh sách các nút theo thứ tự được thêm vào."""
        return list(self._adj)

    def number_of_nodes(self):
        return len(self._adj)

    def number_of_edges(self):
        # Mỗi cạnh được đếm hai lần (ở cả hai đầu)
        return sum(len(nb) for nb in self._adj.values()) // 2

    def degree(self, u):
        """Bậc của nút u (số hàng xóm)."""
        return len(self.neighbors(u))

    def __contains__(self, u):
        return u in self._adj

    def __len__(self):
        return len(self._adj)
