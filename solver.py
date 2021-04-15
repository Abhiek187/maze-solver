from graph import Graph
from paths import Paths
from sys import argv
from time import time


def main():
    # TODO: Generate a random maze: https://en.wikipedia.org/wiki/Maze_generation_algorithm
    # The input contains pairs of vertices that are connected
    # maze1 is based on the maze from slide 20 of the graphs slides
    # maze2 and maze3 are based on the mazes from
    # https://en.wikipedia.org/wiki/Maze-solving_algorithm
    assert len(argv) > 1, "No text file provided."

    with open(argv[1], "r") as file:
        # The first line contains the total number of vertices in the graph
        total_vs = int(file.readline().rstrip())
        # The second line contains the total number of edges in the graph
        total_es = int(file.readline().rstrip())
        maze = Graph(total_vs, total_es)

        for line in file:
            # Remove the newline and split each number
            vs_str = line.rstrip().split()
            # Convert the strings to ints
            vs = list(map(int, vs_str))
            # Connect the two vertices together
            maze.connect(vs[0], vs[1])

        # Print the adjacency list
        # for v in range(maze.vertices):
        #     print(f"{v}: {maze.adj[v]}")

        # Create paths from start to end
        source = 0
        goal = total_vs - 1
        # Time each method of solving the maze
        start = time()
        path_dfs = Paths(maze, source, use_dfs=True).path_to(goal)
        time_dfs = time() - start

        start = time()
        path_bfs = Paths(maze, source, use_dfs=False).path_to(goal)
        time_bfs = time() - start

        start = time()
        path_mouse = maze.random_mouse(source, goal)
        time_mouse = time() - start

        # Print the results
        print(f"Paths from {source} to {goal}\n")

        print("DFS")
        print(f"Path: {path_dfs}")
        print(f"Length: {len(path_dfs)}")
        print(f"Time: {time_dfs} s\n")

        print("BFS")
        print(f"Path: {path_bfs}")
        print(f"Length: {len(path_bfs)}")
        print(f"Time: {time_bfs} s\n")

        print("Random Mouse")
        print(f"Path: {path_mouse}")
        print(f"Length: {len(path_mouse)}")
        print(f"Time: {time_mouse} s")


if __name__ == "__main__":
    main()
