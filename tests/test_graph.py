import networkx as nx
import pytest

from helpers import from_networkx
from sna.graph import Graph


def test_add_edge_skips_self_loop_and_duplicate():
    g = Graph()
    assert g.add_edge(1, 2)
    assert not g.add_edge(2, 1)  # cạnh trùng, đảo chiều
    assert not g.add_edge(3, 3)  # cạnh tự nối
    assert g.number_of_edges() == 1
    assert g.number_of_nodes() == 2
    assert 3 not in g


def test_add_node_isolated():
    g = Graph()
    g.add_node("a")
    g.add_node("a")
    assert g.nodes() == ["a"]
    assert g.degree("a") == 0
    assert g.number_of_edges() == 0


def test_neighbors_missing_node():
    with pytest.raises(KeyError):
        Graph().neighbors(0)


def test_karate_club_matches_networkx():
    nx_g = nx.karate_club_graph()
    g = from_networkx(nx_g)

    assert g.number_of_nodes() == nx_g.number_of_nodes()
    assert g.number_of_edges() == nx_g.number_of_edges()
    assert sorted(g.nodes()) == sorted(nx_g.nodes())
    for u in nx_g.nodes():
        assert g.degree(u) == nx_g.degree(u)
        assert g.neighbors(u) == set(nx_g.neighbors(u))
