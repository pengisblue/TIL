from collections import deque
import sys
sys.stdin = open('input.txt')


def dfs():
    stack = deque([start])
    visited = [[0]*16 for _ in range(16)]
    while stack:
        i, j = stack.pop()
        visited[i][j] = 1
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            dx, dy = i + di, j + dj
            if (dx, dy) == end:
                return 1
            if 0 <= dx < 16 and 0 <= dy < 16:
                if maze[dx][dy] == 0 and visited[dx][dy] == 0:
                    stack.append((dx, dy))

    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    print(f'#{tc} {dfs()}')
