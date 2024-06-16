graph = {}
def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def create_graph():
    n = int(input("Enter the number of edges: "))
    for i in range(n):
        node1 = input("Enter Node 1: ")
        node2 = input("Enter Node 2: ")
        add_edge(node1, node2)
    return graph 

def dfs(graph, start):
    visited = [] 
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

graph = create_graph()
start_node = input("Enter start node: ")
dfs(graph, start_node)