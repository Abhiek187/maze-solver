from graph import LinkedList


class Paths:
    def __init__(self, graph, source, use_dfs):
        self.graph = graph
        self.source = source
        self.visited = [False for _ in range(graph.vertices)]
        self.edge_to = [-1 for _ in range(graph.vertices)]

        # Initialize self.visited and self.edge_to using either DFS or BFS
        if use_dfs:
            self.dfs(self.source)
        else:
            self.bfs(self.source)

    def dfs(self, v):
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
                self.dfs(curr.value)

            curr = curr.next

    def bfs(self, s):
        # Find all the paths connected to the source in BFS order
        queue = LinkedList()  # use a linked list as a queue
        queue.insert(s)
        self.visited[s] = True

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

    def has_path_to(self, v):
        # A path is present if the vertex has been visited
        return self.visited[v]

    def path_to(self, v):
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
