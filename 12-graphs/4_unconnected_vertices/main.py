class Graph:
    def unconnected_vertices(self) -> list[int]:
        unconnected = []
        for vertex, connections in self.graph.items():
            if not connections:
                unconnected.append(vertex)
        return unconnected

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

    def add_node(self, u: int) -> None:
        if u not in self.graph:
            self.graph[u] = set()
