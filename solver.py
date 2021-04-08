from graph import Graph
from paths import Paths
from sys import argv


def main():
    # TODO: Generate a random maze: https://en.wikipedia.org/wiki/Maze_generation_algorithm
    # The input contains pairs of vertices that are connected
    # maze1 is based on the maze from slide 20 of the graphs slides
    # maze2 and maze3 are based on the mazes from
    # https://en.wikipedia.org/wiki/Maze-solving_algorithm
    # maze4 is two disjoint loops
    assert len(argv) > 1, "No text file provided."

    with open(argv[1], "r") as file:
        # The first line contains the total number of vertices in the graph
        total_vs = int(file.readline().rstrip())
        maze = Graph(total_vs)

        for line in file:
            # Remove the newline and split each number
            vs_str = line.rstrip().split()
            # Convert the strings to ints
            vs = list(map(int, vs_str))
            # Connect the two vertices together
            maze.connect(vs[0], vs[1])

        # Print the adjacency list
        for v in range(maze.vertices):
            print(f"{v}: {maze.adj[v]}")

        # Create paths from start to end
        start = 0
        end = total_vs - 1
        path_dfs = Paths(maze, start, use_dfs=True)
        path_bfs = Paths(maze, start, use_dfs=False)
        print(f"Path from {start} to {end} (DFS): {path_dfs.path_to(end)}")
        print(f"Path from {start} to {end} (BFS): {path_bfs.path_to(end)}")


if __name__ == "__main__":
    main()
