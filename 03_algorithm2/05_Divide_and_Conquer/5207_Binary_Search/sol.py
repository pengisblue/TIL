import sys
sys.stdin = open('input.txt')


def binary_search(target, left, right, direction):
    global cnt
    if left > right:
        return
    mid = (left + right) // 2
    if A[mid] == target:
        cnt += 1
    elif direction != 'left' and A[mid] > target:
        binary_search(target, left, mid-1, 'left')
    elif direction != 'right' and A[mid] < target:
        binary_search(target, mid+1, right, 'right')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        binary_search(B[i], 0, N-1, '?')

    print(f'#{tc} {cnt}')
