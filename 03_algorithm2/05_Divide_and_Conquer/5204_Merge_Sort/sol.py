from collections import deque
import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = deque(), deque()
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, len(arr)):
        right.append(arr[i])

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = deque()
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif left:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)
    print(f'#{tc} {ans[N//2]} {cnt}')
