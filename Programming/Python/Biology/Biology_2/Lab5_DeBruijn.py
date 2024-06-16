def build_de_bruijn_graph(seq, k):
    graph = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
    return graph


seq = input("Enter sequence: ")#taatgccatgggatgtt
k = int(input("Enter k-mer length: "))
graph = build_de_bruijn_graph(seq, k)
for node, neighbors in graph.items():
    print(f"{node} -> {', '.join(neighbors)}")


