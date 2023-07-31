import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_V = arr[0]  # or 1000000 (문제에 주어진 최댓값)
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_V > arr[i]:
            min_V = arr[i]

    ans = max_v - min_V
    print(f'#{tc} {ans}')
