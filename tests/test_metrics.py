import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from pprint import pprint
from pygraph import Graph


def test_indegree(small_directed: Graph, small_undirected: Graph):
    assert small_undirected.indegree("a") == 1
    assert small_undirected.indegree("b") == 3
    assert small_undirected.indegree("c") == 2
    assert small_undirected.indegree("d") == 2

    assert small_directed.indegree("a") == 0
    assert small_directed.indegree("b") == 1
    assert small_directed.indegree("c") == 1
    assert small_directed.indegree("d") == 2


def test_outdegree(small_directed: Graph, small_undirected: Graph):
    assert small_undirected.outdegree("a") == 1
    assert small_undirected.outdegree("b") == 3
    assert small_undirected.outdegree("c") == 2
    assert small_undirected.outdegree("d") == 2

    assert small_directed.outdegree("a") == 1
    assert small_directed.outdegree("b") == 2
    assert small_directed.outdegree("c") == 1
    assert small_directed.outdegree("d") == 0


def test_shortest_path(small_directed: Graph, small_undirected: Graph):
    assert small_undirected.get_shortest_path("a", "b") == ["a", "b"]
    assert small_undirected.get_shortest_path("c", "d") == ["c", "d"]
    assert small_undirected.get_shortest_path("a", "d") == ["a", "b", "d"]
    assert small_undirected.get_shortest_path("c", "a") == ["c", "b", "a"]

    assert small_directed.get_shortest_path("a", "b") == ["a", "b"]
    assert small_directed.get_shortest_path("c", "d") == ["c", "d"]
