class Graph:
    """
    1. Initialize tracking structures:
        - Create a list to track visited vertices
        - Create a list to use as a queue for vertices waiting to be explored
    2. Begin the search
        - Add the starting vertex v to the queue
    3. Process the queue until empty:
        - Remove the first vertex from the queue and add it to the visited list
        - Get a sorted list of this vertex's neighbors
        - For each neighbor, if it is neither visited nor queued, add it to the queue
    4. When complete, return the visited list containing vertices in the order they were discovered
    """
    def breadth_first_search(self, v: str) -> list[str]:
        visited = []
        queue = [v]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)
                neighbors = sorted(self.graph[current_vertex])
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

        return visited
            
    # don't touch below this line

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u: str, v: str) -> None:
        if u in self.graph.keys():\
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self) -> str:
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
