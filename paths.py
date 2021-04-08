from graph import Graph
from linked_list import LinkedList
from typing import List


class Paths:
    def __init__(self, graph: Graph, source: int, use_dfs: bool):
        self.graph = graph
        self.source = source  # the starting point in the maze
        # Marks if the vertex is accessible from the source
        self.visited = [False for _ in range(graph.vertices)]
        # The path to each vertex (edge_to[x] = y means that there's a path from y to x)
        self.edge_to = [-1 for _ in range(graph.vertices)]

        # Initialize self.visited and self.edge_to using either DFS or BFS
        if use_dfs:
            self.dfs(self.source)
        else:
            self.bfs(self.source)

    def dfs(self, v: int):
        # Find all the paths connected to the source in DFS order
        if self.visited[v]:
            return

        self.visited[v] = True

        # Iterate through the linked list in v's adjacency list
        curr = self.graph.adj[v].head

        while curr is not None:
            # curr.value connects to v
            if not self.visited[curr.value]:
                self.edge_to[curr.value] = v
                self.dfs(curr.value)  # recursion acts as the stack

            curr = curr.next

    def bfs(self, source: int):
        # Find all the paths connected to the source in BFS order
        queue = LinkedList()  # use a linked list as a queue
        queue.insert(source)
        self.visited[source] = True

        # Keep going until the queue is empty
        while queue.head is not None:
            v = queue.remove_head().value

            # Iterate through the linked list in v's adjacency list
            curr = self.graph.adj[v].head

            while curr is not None:
                # curr.value connects to v
                if not self.visited[curr.value]:
                    queue.insert(curr.value)
                    self.visited[curr.value] = True
                    self.edge_to[curr.value] = v

                curr = curr.next

    def has_path_to(self, v: int) -> bool:
        # A path is present if the vertex has been visited
        return self.visited[v]

    def path_to(self, v: int) -> List:
        # Return a list of vertices that mark the path from the source to v
        if not self.has_path_to(v):
            return []

        x = v
        path = []

        while x != self.source:
            # Add to the beginning of the list and shift all existing elements to the right
            path.insert(0, x)
            x = self.edge_to[x]

        path.insert(0, self.source)
        return path
