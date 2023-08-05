import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for i in range(N)]
    ruins = []  # 유물 길이 리스트
    length_row, length_col = 0, 0   # 유물 길이
    result = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                length_row += 1
                if j+1 >= M or area[i][j+1] == 0:    # 다음 칸은 유물이 없음
                    if length_row > 1:  # 길이가 2 이상일 때
                        ruins.append(length_row)
                    length_row = 0  # 길이 초기화
    for j in range(M):
        for i in range(N):
            if area[i][j] == 1:
                length_col += 1
                if i+1 >= N or area[i+1][j] == 0:    # 다음 칸은 유물이 없음
                    if length_col > 1:
                        ruins.append(length_col)
                    length_col = 0

    for ruin in ruins:
        if result < ruin:
            result = ruin

    print(f'#{tc} {result}')
