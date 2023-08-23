import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    max_v = 0
    for i in range(N):
        for j in range(M):
            sum_v = matrix[i][j]
            for k in range(4):
                if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:
                    sum_v += matrix[i+di[k]][j+dj[k]]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
