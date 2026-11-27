"""Hàm hỗ trợ cho test."""

from sna.graph import Graph


def from_networkx(g):
    """Chuyển đồ thị NetworkX sang Graph của mình (chỉ dùng để đối chiếu trong test)."""
    graph = Graph()
    for u in g.nodes():
        graph.add_node(u)
    for u, v in g.edges():
        graph.add_edge(u, v)
    return graph
