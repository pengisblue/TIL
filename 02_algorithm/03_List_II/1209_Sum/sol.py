import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    test = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    max_v = 0  # 최댓값

    # 행의 합
    for i in range(100):
        tmp = 0  # 합을 담을 임시 변수
        for j in range(100):
            tmp += arr[i][j]
        if max_v < tmp:
            max_v = tmp

    # 열의 합
    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += arr[i][j]
        if max_v < tmp:
            max_v = tmp

    # 대각선의 합
    for k in range(2):
        tmp = 0
        for i in range(100):
            tmp += arr[i][i + (99-2*i)*k]
        if max_v < tmp:
            max_v = tmp

    print(f'#{tc} {max_v}')
