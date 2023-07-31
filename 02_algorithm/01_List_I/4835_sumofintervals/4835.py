import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for index in range(N-M+1):
        interval = 0
        for i in range(M):
            interval += arr[index + i]
        if index == 0:
            min_sum, max_sum = interval, interval
        else:
            if min_sum > interval:
                min_sum = interval
            if max_sum < interval:
                max_sum = interval
    result = max_sum - min_sum
    print(f'#{tc} {result}')
