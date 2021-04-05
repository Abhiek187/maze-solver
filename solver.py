from graph import Graph
from sys import argv


def main():
    # TODO: Generate a random maze
    # The input contains pairs of vertices that are connected
    # maze1.txt is based on the maze from slide 20 of the graphs slides
    assert len(argv) > 1, "No text file provided."

    with open(argv[1], "r") as file:
        maze = Graph(34)  # 34 vertices in maze1

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


if __name__ == "__main__":
    main()
