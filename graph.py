from linked_list import LinkedList


class Graph:
    def __init__(self, max_v: int):
        # Initialize the adjacency list for max_v vertices
        self.adj = [LinkedList() for _ in range(max_v)]  # each linked list is a separate object
        self.vertices = max_v
        self.edges = 0

    def connect(self, v1: int, v2: int):
        # Add an edge connecting v1 to v2 if it doesn't already exist
        if self.adj[v1].insert(v2) and self.adj[v2].insert(v1):
            self.edges += 1
