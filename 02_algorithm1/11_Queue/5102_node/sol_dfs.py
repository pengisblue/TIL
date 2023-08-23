from collections import deque
import sys
sys.stdin = open('input.txt')


def dfs(start, end):
    stack = deque([start])
    visited = [0] * (V+1)
    visited[start] = 1
    while stack:
        now = stack.pop()
        for i in graph[now]:    # now의 인접 정점을 순회하면서
            if i == end:    # 도착지 이면
                return visited[now]     # now까지의 방문 횟수 리턴
            if visited[i] == 0:     # 아직 방문하지 않았다면
                stack.append(i)     # push
                visited[i] = visited[now] + 1   # 방문 횟수 + 1
    # 연결 되어 있지 않음
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())
    print(f'#{tc}', dfs(S, G))
