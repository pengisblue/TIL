import sys
sys.stdin = open('input.txt')


def dfs():
    stack = [start]     # 깊이 탐색할 stack
    di = [-1, 0, 1, 0]  # 델타 탐색할 인덱스
    dj = [0, 1, 0, -1]
    visited = [[0]*N for _ in range(N)]     # 방문 표시
    while stack:
        now = stack.pop()
        visited[now[0]][now[1]] = 1     # 방문
        for idx in range(4):    # 상하좌우 4방향에 대해
            dx = now[0] + di[idx]   # 이동한 행 좌표
            dy = now[1] + dj[idx]   # 이동한 열 좌표
            if (dx, dy) == goal:    # 목적지 좌표와 같으면
                return 1            # 1 반환
            if 0 <= dx < N and 0 <= dy < N:
                # 미로의 통로이면서 아직 방문하지 않았다면
                if maze[dx][dy] == 0 and visited[dx][dy] == 0:
                    stack.append((dx, dy))  # 스택에 추가
    return 0    # 목적지를 찾지 못했다면 0 반환


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:     # 시작 좌표
                start = (i, j)
            elif maze[i][j] == 3:   # 도착 좌표
                goal = (i, j)

    print(f'#{tc}', dfs())
