import sys
sys.stdin = open('input.txt')


def recur(i, j):
    global able
    visited[i][j] = 1
    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        dx, dy = i + di, j + dj
        if (dx, dy) == end:
            able = True
        if 0 <= dx < 16 and 0 <= dy < 16:
            if maze[dx][dy] == 0 and visited[dx][dy] == 0:
                recur(dx, dy)


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    able = False
    visited = [[0] * 16 for _ in range(16)]
    recur(*start)
    if able:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
