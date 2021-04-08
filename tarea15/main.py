class Graph:
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertexes:
            self.vertexes.append(vertex)

    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.edges.append([vertex1, vertex2, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_spanning_tree(self):
        result = []

        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(len(self.vertexes)):
            parent.append(node)
            rank.append(0)

        i, e = 0, 0
        while e < len(self.vertexes) - 1:
            u, v, w = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        return result
