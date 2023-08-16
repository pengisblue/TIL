import sys
sys.stdin = open('input.txt')


def dfs(node, goal):    # 시작, 경로를 찾을 node
    stack = [node]
    visited = [False] * (V+1)
    while stack:
        start = stack.pop()
        if visited[start] == 0:
            visited[start] = True
            for link in range(1, V+1):
                if link == goal and matrix[start][link] == 1:    # 목적지에 이어지면
                    return 1        # 1을 반환하고 종료
                if matrix[start][link] == 1 and visited[link] == 0:
                    stack.append(link)

    else:   # 목적지에 도달하지 못했음
        return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        e1, e2 = map(int, input().split())
        matrix[e1][e2] = 1      # 간선 표시

    S, G = map(int, input().split())
    print(f'#{tc}', dfs(S, G))
