import sys
sys.stdin = open('input.txt')


def route(idx, spend):
    global min_spend
    if idx == N:    # 모든 구역을 방문했을 때
        # 구역을 돌면서 사용한 배터리 + 사무실로 돌아오는 배터리
        total = spend + arr[visited[idx-1]][0]
        if total < min_spend:
            min_spend = total
            return
    for area in range(1, N):    # 0번은 사무실
        if area in visited:
            continue
        # 방문하지 않았으면 idx번째 visited는 area
        visited[idx] = area
        # visited[idx-1] : 이전에 방문한 area
        route(idx+1, spend+arr[visited[idx-1]][visited[idx]])
        # arr[visited[idx - 1]][visited[idx]] : 이전 구역에서 현재구역으로 이동하는데 필요한 배터리 양
        visited[idx] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_spend = N**2*100
    # 방문한 구역을 저장할 리스트
    visited = [0] * N
    route(1, 0)
    print(f'#{tc}', min_spend)
