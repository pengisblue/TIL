from collections import deque
import sys
sys.stdin = open('input.txt')


def dfs(departure, arrival):
    stack = deque([departure])      # 시작점을 enQueue
    visited = [[0] * N for _ in range(N)]   # 방문 확인 + 몇 번째 방문인지
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    while stack:
        now = stack.pop()
        for k in range(4):  # 인접 정점 4방향 탐색
            dx = now[0] + di[k]
            dy = now[1] + dj[k]
            if arrival == (dx, dy):     # 도착지가 인접 정점이면
                return visited[now[0]][now[1]]      # 현재 정점이 몇 번째 방문인지 리턴
            if 0 <= dx < N and 0 <= dy < N:     # 인덱스 범위 안에서
                if maze[dx][dy] == 0 and visited[dx][dy] == 0:  # 갈 수 있는 곳인데 방문하지 않았으면
                    visited[dx][dy] = visited[now[0]][now[1]] + 1   # 다음 방문 횟수 = 현재 방문횟수 + 1
                    stack.append((dx, dy))
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    print(f'#{tc}', dfs(start, end))
