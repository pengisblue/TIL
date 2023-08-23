import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    max_v = 0
    for i in range(N):
        for j in range(M):
            A = matrix[i][j]
            sum_v = A
            for k in range(4):
                for l in range(1, A+1):
                    if 0 <= i + l * di[k] < N and 0 <= j + l * dj[k] < M:
                        sum_v += matrix[i + l*di[k]][j + l*dj[k]]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
