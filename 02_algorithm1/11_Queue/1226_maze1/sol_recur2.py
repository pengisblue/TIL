import sys
sys.stdin = open('input.txt')


def recur(x, y):
    visited[x][y] = 1
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        dx = x + di
        dy = y + dj
        if (dx, dy) == end:
            return 1
        if maze[dx][dy] == 0 and visited[dx][dy] == 0:
            result = recur(dx, dy)
            if result:
                return result
    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    print(f'#{tc} {recur(*start)}')
