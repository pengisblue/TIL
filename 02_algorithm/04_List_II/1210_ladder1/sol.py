import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    # 시작 위치
    row, col = 99, 0
    col_move = [-1, 1]  # 좌, 우 이동
    for j in range(100):
        if ladder[99][j] == 2:
            col = j
            break
    # 아래에서 부터 사다리 타고 올라가기
    while row > 0:
        row -= 1
        # ladder[row+1][col] = '▲'    # 이동한 길 표시
        for move in col_move:
            if 0 <= col+move < 100 and ladder[row][col+move] == 1:  # 좌/우가 1이면
                while 0 <= col+move < 100 and ladder[row][col+move] == 1:   # 다음 좌/우가 1인 동안 (0이 나오기 전까지)
                    col += move     # 계속 이동
                    # if move == -1:
                    #     ladder[row][col-move] = '◀'     # 이동한 길 표시
                    # else:
                    #     ladder[row][col-move] = '▶'
                break   # 이동이 끝나면 반복문 탈출
    # ladder[row][col] = '●'

    # for i in range(100):
    #     for j in range(100):
    #         print(ladder[i][j], end=' ')
    #     print()

    print(f'#{tc} {col}')   # row == 0 (맨 위)일 때 col 값 
