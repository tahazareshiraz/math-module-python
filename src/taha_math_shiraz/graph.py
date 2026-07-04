from .basics import fabs


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = {}

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u][v] = weight
        if not self.directed:
            self.adj[v][u] = weight

    def remove_edge(self, u, v):
        if u in self.adj and v in self.adj[u]:
            del self.adj[u][v]
        if not self.directed and v in self.adj and u in self.adj[v]:
            del self.adj[v][u]

    def remove_vertex(self, v):
        if v in self.adj:
            del self.adj[v]
        for u in self.adj:
            if v in self.adj[u]:
                del self.adj[u][v]

    def neighbors(self, v):
        return list(self.adj.get(v, {}).keys())

    def weight(self, u, v):
        return self.adj.get(u, {}).get(v, None)

    def vertices(self):
        return list(self.adj.keys())

    def edges(self):
        result = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                edge = (u, v, w)
                if self.directed or (v, u, w) not in seen:
                    result.append(edge)
                    seen.add(edge)
        return result

    def degree(self, v):
        return len(self.adj.get(v, {}))

    def in_degree(self, v):
        if not self.directed:
            return self.degree(v)
        return sum(1 for u in self.adj if v in self.adj[u])

    def out_degree(self, v):
        return len(self.adj.get(v, {}))

    def has_edge(self, u, v):
        return v in self.adj.get(u, {})

    def bfs(self, start):
        visited = []
        queue = [start]
        seen = {start}
        while queue:
            v = queue.pop(0)
            visited.append(v)
            for nb in sorted(self.neighbors(v)):
                if nb not in seen:
                    seen.add(nb)
                    queue.append(nb)
        return visited

    def dfs(self, start):
        visited = []
        stack = [start]
        seen = set()
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            visited.append(v)
            for nb in sorted(self.neighbors(v), reverse=True):
                if nb not in seen:
                    stack.append(nb)
        return visited

    def has_path(self, start, end):
        return end in self.bfs(start)

    def dijkstra(self, start):
        INF = float("inf")
        dist = {v: INF for v in self.adj}
        dist[start] = 0
        prev = {v: None for v in self.adj}
        unvisited = set(self.adj.keys())
        while unvisited:
            u = min(unvisited, key=lambda v: dist[v])
            if dist[u] == INF:
                break
            unvisited.remove(u)
            for v, w in self.adj[u].items():
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return dist, prev

    def shortest_path(self, start, end):
        dist, prev = self.dijkstra(start)
        if dist[end] == float("inf"):
            return None, float("inf")
        path = []
        cur = end
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        return path[::-1], dist[end]

    def bellman_ford(self, start):
        INF = float("inf")
        dist = {v: INF for v in self.adj}
        dist[start] = 0
        for _ in range(len(self.adj) - 1):
            for u in self.adj:
                for v, w in self.adj[u].items():
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        for u in self.adj:
            for v, w in self.adj[u].items():
                if dist[u] + w < dist[v]:
                    raise ValueError("negative cycle detected")
        return dist

    def floyd_warshall(self):
        verts = self.vertices()
        n = len(verts)
        idx = {v: i for i, v in enumerate(verts)}
        INF = float("inf")
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u in self.adj:
            for v, w in self.adj[u].items():
                dist[idx[u]][idx[v]] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return {verts[i]: {verts[j]: dist[i][j] for j in range(n)} for i in range(n)}

    def is_connected(self):
        if not self.adj:
            return True
        start = next(iter(self.adj))
        return len(self.bfs(start)) == len(self.adj)

    def topological_sort(self):
        if not self.directed:
            raise ValueError("topological sort requires a directed graph")
        in_deg = {v: 0 for v in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                in_deg[v] = in_deg.get(v, 0) + 1
        queue = [v for v in in_deg if in_deg[v] == 0]
        result = []
        while queue:
            v = queue.pop(0)
            result.append(v)
            for nb in self.neighbors(v):
                in_deg[nb] -= 1
                if in_deg[nb] == 0:
                    queue.append(nb)
        if len(result) != len(self.adj):
            raise ValueError("graph has a cycle")
        return result

    def minimum_spanning_tree_kruskal(self):
        parent = {v: v for v in self.adj}
        rank = {v: 0 for v in self.adj}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
            return True

        edges = sorted(self.edges(), key=lambda e: e[2])
        mst = []
        for u, v, w in edges:
            if union(u, v):
                mst.append((u, v, w))
        return mst

    def has_cycle_undirected(self):
        parent = {}

        def find(x):
            while parent.get(x, x) != x:
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        for u, v, _ in self.edges():
            if not union(u, v):
                return True
        return False

    def is_bipartite(self):
        color = {}
        for start in self.adj:
            if start in color:
                continue
            queue = [start]
            color[start] = 0
            while queue:
                v = queue.pop(0)
                for nb in self.neighbors(v):
                    if nb not in color:
                        color[nb] = 1 - color[v]
                        queue.append(nb)
                    elif color[nb] == color[v]:
                        return False
        return True

    def connected_components(self):
        visited = set()
        components = []
        for start in self.adj:
            if start not in visited:
                component = self.bfs(start)
                components.append(component)
                visited.update(component)
        return components

    def density(self):
        v = len(self.adj)
        e = len(self.edges())
        if v <= 1:
            return 0.0
        max_edges = v * (v - 1) if self.directed else v * (v - 1) // 2
        return e / max_edges if max_edges > 0 else 0.0

    def vertex_count(self):
        return len(self.adj)

    def edge_count(self):
        return len(self.edges())

    def adjacency_matrix(self):
        from .linalg import Matrix
        verts = sorted(self.vertices())
        n = len(verts)
        idx = {v: i for i, v in enumerate(verts)}
        rows = [[0.0] * n for _ in range(n)]
        for u in self.adj:
            for v, w in self.adj[u].items():
                rows[idx[u]][idx[v]] = w
        return Matrix(rows), verts

    def degree_sequence(self):
        return sorted((self.degree(v) for v in self.adj), reverse=True)

    def eccentricity(self, v):
        dist, _ = self.dijkstra(v)
        return max(d for d in dist.values() if d != float("inf"))

    def diameter(self):
        return max(self.eccentricity(v) for v in self.adj)

    def radius(self):
        return min(self.eccentricity(v) for v in self.adj)

    def center(self):
        r = self.radius()
        return [v for v in self.adj if self.eccentricity(v) == r]


def graph_from_edge_list(edges, directed=False):
    g = Graph(directed=directed)
    for edge in edges:
        if len(edge) == 2:
            g.add_edge(edge[0], edge[1])
        else:
            g.add_edge(edge[0], edge[1], edge[2])
    return g


def graph_complete(n):
    g = Graph()
    for i in range(n):
        for j in range(i + 1, n):
            g.add_edge(i, j)
    return g


def graph_cycle(n):
    g = Graph()
    for i in range(n):
        g.add_edge(i, (i + 1) % n)
    return g


def graph_path(n):
    g = Graph()
    for i in range(n - 1):
        g.add_edge(i, i + 1)
    return g


def graph_star(n):
    g = Graph()
    for i in range(1, n):
        g.add_edge(0, i)
    return g


def traveling_salesman_brute(graph):
    from .combinatorics import permutations_list
    verts = graph.vertices()
    if not verts:
        return [], 0
    start = verts[0]
    rest = [v for v in verts if v != start]
    best_path = None
    best_cost = float("inf")
    for perm in permutations_list(rest):
        path = [start] + list(perm) + [start]
        cost = 0
        valid = True
        for i in range(len(path) - 1):
            w = graph.weight(path[i], path[i + 1])
            if w is None:
                valid = False
                break
            cost += w
        if valid and cost < best_cost:
            best_cost = cost
            best_path = path
    return best_path, best_cost
