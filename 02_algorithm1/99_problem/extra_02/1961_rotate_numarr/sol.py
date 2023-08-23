import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):      # 90도 회전
            print(arr[N-j-1][i], end='')
        print(end=' ')
        for j in range(N):      # 180도 회전
            print(arr[N-i-1][N-j-1], end='')
        print(end=' ')
        for j in range(N):      # 270도 회전
            print(arr[j][N-i-1], end='')
        print()
