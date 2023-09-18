import sys
sys.stdin = open('input.txt')


def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)


def partition(arr, left, right):
    i = left - 1
    j = left
    pivot = arr[right]
    while j < right:
        if arr[j] <= pivot:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f'#{tc} {arr[N // 2]}')
