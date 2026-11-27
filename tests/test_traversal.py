import networkx as nx
import pytest

from helpers import from_networkx
from sna.graph import Graph
from sna.traversal import bfs, connected_components, dfs


def small_disconnected():
    """Đồ thị không liên thông: 2 cụm và 1 nút cô lập."""
    g = nx.Graph()
    g.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (10, 11), (11, 12)])
    g.add_node(99)
    return g


GRAPHS = [nx.karate_club_graph(), small_disconnected()]


@pytest.mark.parametrize("nxg", GRAPHS)
def test_bfs_dfs_visit_whole_component(nxg):
    g = from_networkx(nxg)
    for s in nxg.nodes():
        expected = nx.node_connected_component(nxg, s)
        for order in (bfs(g, s), dfs(g, s)):
            assert order[0] == s
            assert len(order) == len(set(order))  # không nút nào bị lặp
            assert set(order) == expected


@pytest.mark.parametrize("nxg", GRAPHS)
def test_bfs_distance_not_decreasing(nxg):
    g = from_networkx(nxg)
    for s in nxg.nodes():
        dist = nx.single_source_shortest_path_length(nxg, s)
        d = [dist[u] for u in bfs(g, s)]
        assert d == sorted(d)


@pytest.mark.parametrize("nxg", GRAPHS)
def test_dfs_each_node_next_to_visited(nxg):
    g = from_networkx(nxg)
    for s in nxg.nodes():
        order = dfs(g, s)
        for i in range(1, len(order)):
            assert any(g.has_edge(order[i], u) for u in order[:i])


@pytest.mark.parametrize("nxg", GRAPHS)
def test_connected_components_match_networkx(nxg):
    g = from_networkx(nxg)
    ours = sorted(sorted(c) for c in connected_components(g))
    theirs = sorted(sorted(c) for c in nx.connected_components(nxg))
    assert ours == theirs


def test_single_node_graph():
    g = Graph()
    g.add_node(7)
    assert bfs(g, 7) == [7]
    assert dfs(g, 7) == [7]
    assert connected_components(g) == [{7}]


def test_empty_graph():
    g = Graph()
    assert connected_components(g) == []
    with pytest.raises(KeyError):
        bfs(g, 1)


def test_missing_start_node():
    g = from_networkx(small_disconnected())
    with pytest.raises(KeyError):
        bfs(g, 1000)
    with pytest.raises(KeyError):
        dfs(g, 1000)
