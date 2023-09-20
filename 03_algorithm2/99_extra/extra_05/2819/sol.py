from collections import deque
import sys
sys.stdin = open('input.txt')

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i, j):
    queue = deque([(i, j, board[i][j])])
    while queue:
        now = queue.popleft()
        for di, dj in move:
            dx = now[0] + di
            dy = now[1] + dj
            if 0 <= dx < 4 and 0 <= dy < 4:
                tmp = now[2] + board[dx][dy]
                if len(tmp) == 7:
                    numbers.add(tmp)
                else:
                    queue.append((dx, dy, tmp))


T = int(input())
for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    numbers = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j)

    print(f'#{tc} {len(numbers)}')
