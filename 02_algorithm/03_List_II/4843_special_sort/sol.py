import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(10):
        idx = i
        for j in range(i+1, N):
            # max 찾기
            if i % 2 == 0:
                if arr[idx] < arr[j]:
                    idx = j
            # min 찾기
            else:
                if arr[idx] > arr[j]:
                    idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    print(f'#{tc}', *arr[:10])
