class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()

        def dfs_recursive(node):
            visited.add(node)
            print(node, end=" ")

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start_node)

def main():
    graph = Graph()

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        graph.add_edge(u, v)

    start_node = int(input("Enter the starting node: "))
    print("DFS traversal starting from node", start_node, ":")
    graph.dfs(start_node)

if __name__ == "__main__":
    main()
