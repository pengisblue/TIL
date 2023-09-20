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
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    group = 0
    for i in range(M):
        graph[numbers[2*i]].append(numbers[2*i+1])
        graph[numbers[2*i+1]].append(numbers[2*i])

    for i in range(1, N+1):
        if graph[i] and not visited[i]:
            group += 1
            dfs(i)
        elif not graph[i]:
            group += 1

    print(f'#{tc} {group}')
