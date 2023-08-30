from collections import deque
import sys
sys.stdin = open('input.txt')

di = [0, 1]
dj = [1, 0]


def bfs():
    queue = deque([(0, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = arr[0][0]
    while queue:
        i, j = queue.popleft()
        for k in range(2):
            dx = i + di[k]
            dy = j + dj[k]
            if 0 <= dx < N and 0 <= dy < N:
                sum_v = visited[i][j] + arr[dx][dy]
                # 방문한적 있는데 이전 방문보다 값이 작으면
                if visited[dx][dy] and sum_v < visited[dx][dy]:
                    visited[dx][dy] = sum_v
                    queue.append((dx, dy))
                # 방문한 적이 없으면
                elif not visited[dx][dy]:
                    visited[dx][dy] = sum_v
                    queue.append((dx, dy))

    return visited[N-1][N-1]    # 도착지에 저장된 visited값 return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', bfs())
