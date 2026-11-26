import networkx as nx


def test_import_sna():
    import sna

    assert sna.__doc__


def test_karate_club():
    g = nx.karate_club_graph()
    assert g.number_of_nodes() == 34
    assert g.number_of_edges() == 78
