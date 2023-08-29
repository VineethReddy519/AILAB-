from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")
            
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

graph = Graph()

num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))


for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph.add_edge(u, v)


start_node = int(input("Enter the starting node for BFS: "))

print("BFS Traversal:")
graph.bfs(start_node)
