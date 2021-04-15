from linked_list import LinkedList
from random import randrange
from typing import List


class Graph:
    def __init__(self, max_v: int, max_e: int):
        # Initialize the adjacency list for max_v vertices
        self.adj = [LinkedList() for _ in range(max_v)]  # each linked list is a separate object
        self.vertices = max_v
        self.edges = max_e

    def connect(self, v1: int, v2: int):
        # Add an edge connecting v1 to v2
        self.adj[v1].insert(v2)
        self.adj[v2].insert(v1)

    def degree(self, v: int) -> int:
        # Get the number of vertices connected to v
        curr = self.adj[v].head
        deg = 0

        while curr is not None:
            deg += 1
            curr = curr.next

        return deg

    def random_mouse(self, start: int, goal: int) -> List:
        # Gather a log of where the random mouse traveled
        path = [start]
        v = start

        while v != goal:
            # Select a random path at a junction
            rand_path = randrange(0, self.degree(v))  # random number from 0 to degree - 1
            next_node = self.adj[v].head

            # Keep traversing the linked list until the random index is reached
            while rand_path > 0:
                next_node = next_node.next
                rand_path -= 1

            v = next_node.value
            path.append(v)

        return path
