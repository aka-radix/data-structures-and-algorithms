import pytest
from graph_depth_first import __version__
from graph_depth_first.graph_depth_first_search import Graph


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def graph():
    graph = Graph()
    x = graph.add_node("A")
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    f = graph.add_node("f")
    g = graph.add_node("g")
    h = graph.add_node("h")

    graph.add_edge(a, b)
    graph.add_edge(a, d)

    graph.add_edge(b, a)
    graph.add_edge(b, d)
    graph.add_edge(b, c)

    graph.add_edge(c, b)
    graph.add_edge(c, g)

    graph.add_edge(d, a)
    graph.add_edge(d, b)
    graph.add_edge(d, f)
    graph.add_edge(d, h)
    graph.add_edge(d, e)

    graph.add_edge(e, d)

    graph.add_edge(f, d)
    graph.add_edge(f, h)

    graph.add_edge(g, c)

    graph.add_edge(h, d)
    graph.add_edge(h, f)
    return {"graph": graph, "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h}
