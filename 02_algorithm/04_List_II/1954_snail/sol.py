import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for i in range(N)]   # 빈 달팽이
    row, col = 0, 0     # 각 인덱스 값 초기화
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    idx = 0     # di, dj 인덱스

    for i in range(1, N**2+1):
        snail[row][col] = i

    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])
