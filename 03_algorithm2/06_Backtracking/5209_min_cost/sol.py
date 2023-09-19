import sys
sys.stdin = open('input.txt')


def perm(i, cost):
    global min_cost
    if i == N:
        if cost < min_cost:
            min_cost = cost
        return

    if cost >= min_cost:
        return

    for j in range(N):
        if j not in order:
            order[i] = j
            perm(i+1, cost+V[i][j])
            order[i] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    order = [-1] * N
    min_cost = 99 * (N ** 2)
    perm(0, 0)
    print(f'#{tc} {min_cost}')
