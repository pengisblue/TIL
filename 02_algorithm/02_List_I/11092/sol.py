import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0  # 최솟값의 인덱스
    max_idx = 0  # 최댓값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i
    # abs(max_idx-min_idx)
    # max(max_idx, min_idx) - min(max_idx, min_idx)
    ans = max_idx - min_idx
    if ans < 0:
        ans *= -1
    print(f'#{tc} {ans}')