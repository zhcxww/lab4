from typing import Tuple, Union, Iterable
import networkx as nx

Node = Union[str, int]
Edge = Tuple[Node, Node]


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        self.G = {}
        self.directed = directed
        for e in edges:
            self.add_edge(e)

    def has_node(self, node: Node):
        """Whether a node is in graph"""
        return node in self.G

    def has_edge(self, edge: Edge):
        """Whether an edge is in graph"""
        return edge[1] in self.G.get(edge[0], [])

    def add_node(self, node: Node):
        """Add a node"""
        if node not in self.G:
            self.G[node] = []

    def add_edge(self, edge: Edge):

        """Add an edge (node1, node2). For directed graph, node1 -> node2"""
        self.add_node(edge[0])
        self.add_node(edge[1])
        if not self.has_edge(edge):
            self.G[edge[0]].append(edge[1])
            if not self.directed:
                self.G[edge[1]].append(edge[0])

    def remove_node(self, node: Node):
        """Remove all references to node"""
        if self.has_node(node):
            del self.G[node]
            for n in self.G:
                if node in self.G[n]:
                    self.G[n].remove(node)
        else:
            raise ValueError("Invalid")

    def remove_edge(self, edge: Edge):

        """Remove an edge from graph"""
        if self.has_edge(edge):
            self.G[edge[0]].remove(edge[1])
            if not self.directed:
                self.G[edge[1]].remove(edge[0])
        else:
            raise ValueError("Invalid")

    def indegree(self, node: Node) -> int:
        """Compute indegree for a  node"""
        if self.has_node(node):
            if not self.directed:
                return self.outdegree(node)
            indegree = 0
            for n in self.G:
                if node in self.G[n]:
                    indegree += 1
            return indegree
        else:
            raise ValueError("Invalid")

    def outdegree(self, node: Node) -> int:
        """Compute outdegree for a node"""
        if self.has_node(node):
            return len(self.G[node])
        else:
            raise ValueError("Invalid")

    def get_shortest_path(self, node1: Node, node2: Node):
        e = []
        for i in self.G:
            for j in self.G[i]:
                e.append((i, j))
        if self.directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        G.add_edges_from(e)
        return nx.shortest_path(G, node1, node2)

    def __str__(self):
        return f"{self.__class__.__name__}:{self.G}"

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.G}"
