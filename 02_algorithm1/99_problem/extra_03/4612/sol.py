import sys
sys.stdin = open('input.txt')

move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 인덱스의 편의를 위해 N+1 크기의 보드 생성
    board = [[0] * (N+1) for _ in range(N+1)]
    black, white = 0, 0     # 흑돌, 백돌의 개수
    # 초기 세팅
    board[(N//2)+1][(N//2)+1] = 2
    board[N//2][N//2] = 2
    board[(N//2)+1][N//2] = 1
    board[N//2][(N//2)+1] = 1
    for _ in range(M):
        j, i, color = map(int, input().split())
        board[i][j] = color
        # 바꿀 돌이 있는지 확인하기
        for di, dj in move:
            dx = i + di
            dy = j + dj
            if 0 < dx <= N and 0 < dy <= N:
                # 탐색 방향에 다른 색 돌이 있을 때,
                if board[dx][dy] != 0 and board[dx][dy] != color:
                    change = False
                    tmp_i, tmp_j = i+di, j+dj
                    while 0 < tmp_i <= N and 0 < tmp_j <= N:
                        if board[tmp_i][tmp_j] == 0:
                            break   # 바꿀 수 없음
                        # 그 방향의 끝에 같은 색의 돌이 있다면,
                        if board[tmp_i][tmp_j] == color:
                            change = True   # 바꿀 수 있음
                            break
                        tmp_i += di
                        tmp_j += dj
                    # 색깔을 바꿀 수 있을 때
                    if change:
                        # 같은 색 돌을 만날 때 까지
                        while board[dx][dy] != color:
                            board[dx][dy] = color
                            dx += di
                            dy += dj

    # 보드를 순회하며 색깔 카운팅
    for m in range(1, N+1):
        for n in range(1, N+1):
            if board[m][n] == 1:
                black += 1
            elif board[m][n] == 2:
                white += 1

    print(f'#{tc}', black, white)
