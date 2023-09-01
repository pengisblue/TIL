from collections import deque
import sys
sys.stdin = open('input.txt')

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    while queue:
        ni, nj = queue.popleft()
        for di, dj in move:
            dx, dy = ni + di, nj + dj
            if 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == -1:
                visited[dx][dy] = visited[ni][nj] + 1
                queue.append((dx, dy))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    queue = deque()
    result = 0
    # ground = [list(input()) for _ in range(N)]
    for i in range(N):
        # ground를 리스트로 저장하지 않아서 메모리 감소
        ground = list(input())
        for j in range(M):
            if ground[j] == 'W':
                visited[i][j] = 0
                queue.append((i, j))
    bfs()
    for i in range(N):
        for j in range(M):
            result += visited[i][j]

    print(f'#{tc}', result)
