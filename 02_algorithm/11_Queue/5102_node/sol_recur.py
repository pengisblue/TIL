import sys
sys.stdin = open('input.txt')


def recur(s, cnt):
    global able
    if s == G:
        able = cnt
    visited[s] = 1
    for i in graph[s]:
        if visited[i] == 0:
            recur(i, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())
    able = 0
    recur(1, 0)
    print(f'#{tc}', able)
