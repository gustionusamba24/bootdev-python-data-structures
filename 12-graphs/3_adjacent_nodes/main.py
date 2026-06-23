class Graph:
    def adjacent_nodes(self, node: int) -> set[int]:
        return self.graph[node]

    # don't touch below this line

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u: int, v: int) -> None:
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    adjacent_nodes = graph.adjacent_nodes(1)
    print(adjacent_nodes)