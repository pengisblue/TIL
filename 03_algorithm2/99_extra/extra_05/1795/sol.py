from collections import  deque
import sys
sys.stdin = open('input.txt')


def bfs(departure, arrival):
    queue = deque([departure, 0])
    visited = [0] * (N+1)
    visited[departure] = 1
    while queue:
        now, total = queue.popleft()
        for link, time in graph[now]:
            if not


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())     # 정점 갯수, 간선 갯수, 집
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())     # 시작점, 도착점, 시간
        graph[x].append((y, c))

