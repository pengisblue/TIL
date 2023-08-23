import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    board = [[0] * 10 for i in range(10)]  # 0으로 채워진 2차원 배열
    N = int(input())  # 색칠 횟수
    purple = 0  # 3(보라색)의 개수
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if board[row][col] != color:  # board의 숫자랑 color로 받은 숫자가 다를 때
                    if board[row][col] == 0:  # 숫자를 처음 받는 경우
                        board[row][col] = color  # color로 받은 숫자로 바꿔줌
                    elif board[row][col] != 3:  # 1 or 2일 때
                        board[row][col] = 3  # 3(보라색)
                        purple += 1
                    # else: 기존 color가 3(보라색)일 때: pass
                # else: 숫자가 같을 때: pass

    print(f'#{tc} {purple}')
