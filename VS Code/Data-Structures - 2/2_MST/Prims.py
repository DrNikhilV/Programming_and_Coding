graph = {}
def prim(graph):
    mst = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    while visited != set(graph.keys()):
        edges = []
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited:
                    edges.append((u, v, weight))
        u, v, _ = min(edges, key=lambda x: x[2])
        mst.append((u, v))
        visited.add(v)
    return mst

def create_graph():
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input("Enter node: ")
        edges = int(input("Enter the number of edges: "))
        edge_list = []
        for j in range(edges):
            node1 = input("Enter node: ")
            edge1 = int(input("Enter edge weight: "))
            edge_list.append((node1, edge1))
        graph[node] = edge_list
    return graph

graph = create_graph()
mst = prim(graph)
print("Minimum Spanning Tree:")
for node in mst:
    print(node)