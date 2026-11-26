from pathlib import Path

from sna.io import read_edge_list

SAMPLE = Path(__file__).parent / "data" / "sample_edges.txt"


def test_read_sample_edges():
    g, _ = read_edge_list(SAMPLE)

    assert sorted(g.nodes()) == [1, 2, 3, 4, 5]
    assert g.number_of_edges() == 4
    for u, v in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        assert g.has_edge(u, v)
    assert not g.has_edge(3, 3)


def test_read_sample_stats():
    _, stats = read_edge_list(SAMPLE)

    assert stats["lines_read"] == 14
    assert stats["skipped"] == {
        "blank": 2,
        "comment": 2,
        "malformed": 3,
        "self_loop": 1,
        "duplicate": 2,
    }
    assert stats["nodes"] == 5
    assert stats["edges"] == 4


def test_read_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("", encoding="utf-8")
    g, stats = read_edge_list(path)
    assert g.number_of_nodes() == 0
    assert stats["lines_read"] == 0
    assert stats["edges"] == 0
