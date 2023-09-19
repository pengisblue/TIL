import sys
sys.stdin = open('input.txt')


def work(i, acc):
    global max_acc
    if i == N:
        if acc > max_acc:
            max_acc = acc
        return

    if acc == 0:
        return

    if max_acc > acc:
        return

    for j in range(N):
        if j not in order:
            order[i] = j
            work(i+1, acc * (P[i][j]/100))
            order[i] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    order = [-1] * N
    max_acc = 0
    work(0, 1)
    print(f'#{tc} {max_acc * 100:.6f}')
