from linked_list import LinkedList
from math import sqrt
from random import randrange
from typing import List


class Graph:
    def __init__(self, max_v: int):
        # Initialize the adjacency list for max_v vertices
        self.adj = [LinkedList() for _ in range(max_v)]  # each linked list is a separate object
        self.points = [(-1, -1) for _ in range(max_v)]
        self.vertices = max_v
        self.edges = 0

    def __dist(self, v1: int, v2: int) -> float:
        # Use the distance formula
        x1, y1 = self.points[v1]
        x2, y2 = self.points[v2]
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def connect(self, v1: int, v2: int):
        # Calculate the distance from v1 to v2, v1 to the end, and v2 to the end
        weight = self.__dist(v1, v2)
        h1 = self.__dist(v1, self.vertices - 1)
        h2 = self.__dist(v2, self.vertices - 1)
        # Add an edge connecting v1 to v2
        self.adj[v1].insert(v2, weight, h2)
        self.adj[v2].insert(v1, weight, h1)

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
