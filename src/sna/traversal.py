"""Duyệt đồ thị: BFS, DFS và tìm thành phần liên thông."""

from collections import deque


def bfs(graph, start):
    """Duyệt theo chiều rộng từ start, trả về danh sách nút theo thứ tự duyệt.

    Báo KeyError nếu start không có trong đồ thị.
    """
    graph.neighbors(start)  # kiểm tra start có trong đồ thị
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.neighbors(u):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order


def dfs(graph, start):
    """Duyệt theo chiều sâu từ start (dùng stack, không đệ quy).

    Trả về danh sách nút theo thứ tự duyệt. Báo KeyError nếu start không có.
    """
    graph.neighbors(start)
    visited = set()
    order = []
    stack = [start]
    while stack:
        u = stack.pop()
        if u in visited:
            continue  # một nút có thể bị đẩy vào stack nhiều lần
        visited.add(u)
        order.append(u)
        for v in graph.neighbors(u):
            if v not in visited:
                stack.append(v)
    return order


def connected_components(graph):
    """Trả về danh sách các thành phần liên thông, mỗi thành phần là một tập nút."""
    seen = set()
    components = []
    for u in graph.nodes():
        if u not in seen:
            comp = set(bfs(graph, u))
            seen |= comp
            components.append(comp)
    return components
