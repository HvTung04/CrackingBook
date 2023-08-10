class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

def main():
    G = Graph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('B', 'D')
    G.add_edge('C', 'D')
    G.add_edge('E', 'B')
    G.add_edge('E', 'C')
    for node, adj in G.graph.items():
        print(f"Adj of {node} are: {adj}")


if __name__ == "__main__":
    main()