from linked_list import LinkedList
from math import sqrt
from random import randrange
from typing import List


class Graph:
    def __init__(self, max_v: int):
        # Initialize the adjacency list for max_v vertices
        self.adj = [LinkedList() for _ in range(max_v)]  # each linked list is a separate object
        self.points = [(-1, -1) for _ in range(max_v)]
        self.start = 0
        self.goal = max_v - 1
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

    def random_mouse(self) -> List:
        # Gather a log of where the random mouse traveled
        path = [self.start]
        v = self.start

        while v != self.goal:
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

    def wall_follower(self, left_wall: bool) -> List:
        # Keep following either the left or right wall until the goal is reached
        path = [self.start]
        v = self.start
        curr_dir = "down"  # start by facing down at the start point

        while v != self.goal:
            """
            Left Wall:
            If facing down: prioritize right, down, left, up
            If facing left: prioritize down, left, up, right
            If facing up: prioritize left, up, right, down
            If facing right: prioritize up, right, down, left
            
            Right Wall:
            If facing down: prioritize left, down, right, up
            If facing left: prioritize up, left, down, right
            If facing up: prioritize right, up, left, down
            If facing right: prioritize down, right, up, left
            """
            if left_wall:
                if curr_dir == "down":
                    priority_dirs = {"up": 0, "left": 1, "down": 2, "right": 3}
                elif curr_dir == "left":
                    priority_dirs = {"right": 0, "up": 1, "left": 2, "down": 3}
                elif curr_dir == "up":
                    priority_dirs = {"down": 0, "right": 1, "up": 2, "left": 3}
                else:
                    priority_dirs = {"left": 0, "down": 1, "right": 2, "up": 3}
            else:
                if curr_dir == "down":
                    priority_dirs = {"up": 0, "right": 1, "down": 2, "left": 3}
                elif curr_dir == "left":
                    priority_dirs = {"right": 0, "down": 1, "left": 2, "up": 3}
                elif curr_dir == "up":
                    priority_dirs = {"down": 0, "left": 1, "up": 2, "right": 3}
                else:
                    priority_dirs = {"left": 0, "up": 1, "right": 2, "down": 3}

            curr_point = self.points[v]
            next_v = None
            next_dir = curr_dir
            max_priority = -1
            choice = self.adj[v].head

            while choice is not None:
                # Check which direction a vertex is with respect to the current vertex
                choice_point = self.points[choice.value]

                if choice_point[0] < curr_point[0]:
                    choice_dir = "left"
                elif choice_point[0] > curr_point[0]:
                    choice_dir = "right"
                elif choice_point[1] < curr_point[1]:
                    choice_dir = "up"
                else:
                    choice_dir = "down"

                # Check if the direction is of higher priority
                if priority_dirs[choice_dir] > max_priority:
                    next_v = choice.value
                    next_dir = choice_dir
                    max_priority = priority_dirs[choice_dir]

                choice = choice.next

            # Head in the direction that follows the wall
            v = next_v
            path.append(next_v)
            curr_dir = next_dir

        return path
