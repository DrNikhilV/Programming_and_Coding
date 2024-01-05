graph = {}

def add(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def create():
    n = int(input("Enter the number of edges: "))
    for i in range(n):
        node1 = input("Enter Node 1: ")
        node2 = input("Enter Node 2: ")
        add(node1, node2)

def bfs(node):
    visited = {}
    for i in graph:
        visited[i] = False
    queue = []
    queue.append(node)
    visited[node] = True
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for i in graph.get(node, []):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

create()
start_node = input("Enter start node: ")
bfs(start_node)