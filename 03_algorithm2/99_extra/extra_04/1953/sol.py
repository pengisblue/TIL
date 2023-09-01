from collections import deque
import sys
sys.stdin = open('input.txt')

road = {
    0: [(0, 0)],
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}


def bfs():
    global result
    queue = deque([(R, C)])
    visited[R][C] = 1
    while queue:
        i, j = queue.popleft()
        if visited[i][j] == L:
            return result
        move = road[plan[i][j]]
        for di, dj in move:
            dx = i + di
            dy = j + dj
            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy]:
                if (0-di, 0-dj) in road[plan[dx][dy]]:
                    visited[dx][dy] = visited[i][j] + 1
                    result += 1
                    queue.append((dx, dy))
    return result


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    plan = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 1
    print(f'#{tc}', bfs())
