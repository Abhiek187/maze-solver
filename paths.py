from graph import Graph
from linked_list import LinkedList
from math import inf
from minpq import MinPQ
from typing import List


class Paths:
    def __init__(self, graph: Graph):
        self.graph = graph
        # Marks if the vertex is accessible from the source
        self.visited = [False for _ in range(graph.vertices)]
        # The path to each vertex (edge_to[x] = y means that there's a path from y to x)
        self.edge_to = [-1 for _ in range(graph.vertices)]

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

        return self

    def bfs(self):
        # Find all the paths connected to the source in BFS order
        queue = LinkedList()  # use a linked list as a queue
        queue.insert(self.graph.start)
        self.visited[self.graph.start] = True

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

        return self

    def dijkstra(self):
        # Find the shortest route through the maze
        dist_to = [inf for _ in range(self.graph.vertices)]
        dist_to[self.graph.start] = 0  # the distance to the source itself is 0
        self.visited[self.graph.start] = True
        curr_v = self.graph.start
        # A priority queue of each vertex and their shortest distance from the start
        pq = MinPQ(self.graph.edges)
        curr = self.graph.adj[curr_v].head

        # Add each neighboring vertex to the priority queue
        while curr is not None:
            dist_to[curr.value] = curr.weight
            self.edge_to[curr.value] = curr_v
            pq.insert([curr.value, curr.weight])
            curr = curr.next

        while not pq.is_empty():
            # Remove the next shortest vertex
            curr_v, _ = pq.del_min()
            self.visited[curr_v] = True

            # Exit early if the goal was reached
            if curr_v == self.graph.goal:
                return self

            curr = self.graph.adj[curr_v].head

            while curr is not None:
                if not self.visited[curr.value]:
                    # If an edge shortens the distance to a vertex, update the shortest distance
                    if dist_to[curr_v] + curr.weight < dist_to[curr.value]:
                        dist_to[curr.value] = dist_to[curr_v] + curr.weight
                        self.edge_to[curr.value] = curr_v
                        pq.update_or_insert([curr.value, dist_to[curr.value]])

                curr = curr.next

        return self

    def has_path_to(self, v: int) -> bool:
        # A path is present if the vertex has been visited
        return self.visited[v]

    def path_to(self, v: int) -> List:
        # Return a list of vertices that mark the path from the source to v
        if not self.has_path_to(v):
            return []

        x = v
        path = []

        while x != self.graph.start:
            # Add to the beginning of the list and shift all existing elements to the right
            path.insert(0, x)
            x = self.edge_to[x]

        path.insert(0, self.graph.start)
        return path
