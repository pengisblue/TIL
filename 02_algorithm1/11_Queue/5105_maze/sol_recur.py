import sys
sys.stdin = open('input.txt')


def recur(i, j):
    global able
    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        dx, dy = i + di, j + dj
        if (dx, dy) == end:
            able = visited[i][j]
        if 0 <= dx < N and 0 <= dy < N:
            if maze[dx][dy] == 0 and visited[dx][dy] == 0:
                visited[dx][dy] = visited[i][j] + 1
                recur(dx, dy)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   # 방문 확인 + 몇 번째 방문인지
    able = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    visited[start[0]][start[1]] = 0
    recur(*start)
    print(f'#{tc} {able}')
