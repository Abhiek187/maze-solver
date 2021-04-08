from graph import Graph
from paths import Paths
from sys import argv


def main():
    # TODO: Generate a random maze
    # The input contains pairs of vertices that are connected
    # maze1.txt is based on the maze from slide 20 of the graphs slides
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

        # Create paths from the first vertex
        path0 = Paths(maze, 0, use_dfs=True)
        print(f"Path from 0 to 33: {path0.path_to(33)}")


if __name__ == "__main__":
    main()
