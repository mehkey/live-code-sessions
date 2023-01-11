# Shortest Cell Path

In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
Constraints:

[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer


    M = len(grid)
    N = len(grid[0])

    q = deque()

    q.add([sr,sc])

    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    grid[x][y] = 0

    dist = 0

    while q:
        
        for _ in range(len(q)):

            x,y = q.popleft()
            
            if x == tr and y == tc:
                return dist

            for dir in dirs:
                x_new = x + dir[0]
                y_new = y + dir[1]

                if 0 <= x_new < M and 0 <= y_new < N and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 0
                    q.add([x_new,y_new])
        dist += 1

    return -1
