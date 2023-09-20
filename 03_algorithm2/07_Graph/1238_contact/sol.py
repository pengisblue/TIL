from collections import deque
import sys
sys.stdin = open('input.txt')


def dfs(n):
    queue = deque([n])
    visited[n] = 1
    while queue:
        now = queue.popleft()
        for link in graph[now]:
            if not visited[link]:
                visited[link] = visited[now] + 1
                queue.append(link)


T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(0, N, 2):
        graph[from_to[i]].append(from_to[i+1])

    dfs(start)
    last = max(visited)
    for i in range(100, -1, -1):
        if visited[i] == last:
            result = i
            break

    print(f'#{tc}', result)
