import sys
sys.stdin = open('input.txt')


def dfs(n):
    stack = [n]
    while stack:
        now = stack.pop()
        visited[now] = 1
        for link in graph[now]:
            if not visited[link]:
                stack.append(link)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 전체 사람 수 , 관계 수
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            dfs(i)

    print(f'#{tc}', cnt)