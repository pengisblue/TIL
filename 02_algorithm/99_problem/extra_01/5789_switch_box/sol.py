import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())    # 상자의 개수, 작업 횟수
    boxs = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        boxs[L-1:R] = [i] * (R-L+1)

    print(f'#{tc}', *boxs)
