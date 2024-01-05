class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
    
    def add(self, u, v, w):
        self.edges.append((u, v, w))

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        parent = [i for i in range(self.V)]
        mst = []
        edges_in_mst = 0

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for edge in self.edges:
            u, v, w = edge
            if find(u) != find(v):
                mst.append((u, v, w))
                union(u, v)
                edges_in_mst += 1
                if edges_in_mst == self.V - 1:
                    break

        return mst

# Example usage:
g = Graph(4)
g.add(0, 1, 10)
g.add(0, 2, 6)
g.add(0, 3, 5)
g.add(1, 3, 15)
g.add(2, 3, 4)

mst = g.kruskal()
for u, v, w in mst:
    print(f"Edge: {u}-{v}, Weight: {w}")
