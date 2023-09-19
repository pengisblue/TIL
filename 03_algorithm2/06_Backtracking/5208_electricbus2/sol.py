from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs():
    queue = deque([1])
    while queue:
        stop = queue.popleft()
        energy = M[stop]
        for i in range(stop+energy, stop, -1):
            if i >= N:
                return visited[stop]
            if not visited[i]:
                visited[i] = visited[stop] + 1
                queue.append(i)


T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split()))
    N = M[0]
    visited = [0] * N
    print(f'#{tc} {bfs()}')
