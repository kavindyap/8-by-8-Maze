from collections import deque
import random

# Define a function with input as maze
def solve_maze(maze):
    R, C = len(maze), len(maze[0])  # R, C Rows and Column of the maze

    start = (0, 0)
    for r in range(R):          # Identification of starting point of the maze
        for c in range(C):
            if maze[r][c] == "S":
                start = (r, c)
                break
        else: continue
        break
    else:
        return None

    # Algorithm for BFS

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:

        coord = queue.pop()
        visited[coord[0]][coord[1]] = True
        print((coord[0], coord[1]))         # print reached coordinates
        if maze[coord[0]][coord[1]] == "G":
            return coord[2]

        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]:
                continue
            queue.appendleft((nr, nc, coord[2]+1))

        # Select maze randomly, from saved files

maze_file = ['maze1.txt', 'maze2.txt', 'maze3.txt']
maze_file_random = random.choice(maze_file)

        # open saved text file as a maze

with open(maze_file_random) as file:
    maze = []
    for line in file:
        maze.append([i for i in line.strip("\n")])

    # Print minimum coordinates to gaol & randomly selected maze

print("Minimum nodes to start point to gaol is (BFS) = ", + solve_maze(maze))
print("Randomly selected maze = ", maze_file_random)

