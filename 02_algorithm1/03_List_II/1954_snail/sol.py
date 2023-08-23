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

    for num in range(1, N**2+1):
        snail[row][col] = num
        # 다음으로 갈 방향이 snail 범위 안이고, 다음 칸에 숫자가 없을 때
        if (0 <= row+di[idx] < N) and (0 <= col+dj[idx] < N) and snail[row+di[idx]][col+dj[idx]] == 0:
            pass
        else:   # 방향 전환
            idx += 1
            if idx == 4:  # 인덱스 값이니까 4가 되면 0으로
                idx = 0
        row += di[idx]
        col += dj[idx]

    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])
