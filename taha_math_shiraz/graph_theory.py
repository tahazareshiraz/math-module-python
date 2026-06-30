class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency[u][v] = weight
        if not self.directed:
            self.adjacency[v][u] = weight

    def remove_edge(self, u, v):
        if v in self.adjacency.get(u, {}):
            del self.adjacency[u][v]
        if not self.directed and u in self.adjacency.get(v, {}):
            del self.adjacency[v][u]

    def remove_vertex(self, vertex):
        self.adjacency.pop(vertex, None)
        for neighbors in self.adjacency.values():
            neighbors.pop(vertex, None)

    def neighbors(self, vertex):
        return list(self.adjacency.get(vertex, {}).keys())

    def vertices(self):
        return list(self.adjacency.keys())

    def edges(self):
        result = []
        seen = set()
        for u in self.adjacency:
            for v, w in self.adjacency[u].items():
                key = (u, v) if self.directed else tuple(sorted([u, v]))
                if key not in seen:
                    seen.add(key)
                    result.append((u, v, w))
        return result

    def degree(self, vertex):
        return len(self.adjacency.get(vertex, {}))

    def has_edge(self, u, v):
        return v in self.adjacency.get(u, {})

    def breadth_first_search(self, start):
        visited = [start]
        queue = [start]
        while queue:
            current = queue.pop(0)
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

    def depth_first_search(self, start):
        visited = []
        stack = [start]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                for neighbor in reversed(self.neighbors(current)):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited

    def is_connected(self):
        if not self.adjacency:
            return True
        start = next(iter(self.adjacency))
        visited = self.breadth_first_search(start)
        return len(visited) == len(self.adjacency)

    def shortest_path_unweighted(self, start, end):
        if start == end:
            return [start]
        visited = {start}
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    if neighbor == end:
                        return new_path
                    visited.add(neighbor)
                    queue.append(new_path)
        return None

    def dijkstra(self, start):
        distances = {v: float("inf") for v in self.adjacency}
        distances[start] = 0
        unvisited = set(self.adjacency.keys())
        while unvisited:
            current = min(unvisited, key=lambda v: distances[v])
            unvisited.remove(current)
            if distances[current] == float("inf"):
                break
            for neighbor, weight in self.adjacency[current].items():
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        return distances

    def has_cycle(self):
        visited = set()

        def visit(vertex, parent):
            visited.add(vertex)
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    if visit(neighbor, vertex):
                        return True
                elif self.directed or neighbor != parent:
                    return True
            return False

        for vertex in self.adjacency:
            if vertex not in visited:
                if visit(vertex, None):
                    return True
        return False

    def topological_sort(self):
        if not self.directed:
            raise ValueError("topological sort requires a directed graph")
        visited = set()
        order = []

        def visit(vertex):
            visited.add(vertex)
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    visit(neighbor)
            order.append(vertex)

        for vertex in self.adjacency:
            if vertex not in visited:
                visit(vertex)
        return order[::-1]

    def connected_components(self):
        visited = set()
        components = []
        for vertex in self.adjacency:
            if vertex not in visited:
                component = self.breadth_first_search(vertex)
                visited.update(component)
                components.append(component)
        return components

    def adjacency_matrix(self, vertex_order=None):
        vertices = vertex_order or self.vertices()
        index = {v: i for i, v in enumerate(vertices)}
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]
        for u, v, w in self.edges():
            matrix[index[u]][index[v]] = w
            if not self.directed:
                matrix[index[v]][index[u]] = w
        return matrix


def complete_graph(n):
    g = Graph(directed=False)
    for i in range(n):
        for j in range(i + 1, n):
            g.add_edge(i, j)
    return g


def path_graph(n):
    g = Graph(directed=False)
    for i in range(n - 1):
        g.add_edge(i, i + 1)
    return g


def cycle_graph(n):
    g = path_graph(n)
    if n > 2:
        g.add_edge(n - 1, 0)
    return g
