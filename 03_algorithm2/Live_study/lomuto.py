def quick_sort(arr, left, right):   # 배열, 왼쪽, 오른쪽 idx
    # 분할 정복의 가장 핵심
    # 정복 대상의 범위를 가장 작아질 때 까지 쪼갠다.
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)

# 피봇은 가장 오른쪽 원소
def cal(arr, left, right):
    # 피봇보다 큰 구간의 왼쪽 경계
    i = left - 1
    # 피봇보다 큰 구간의 오른쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        if pivot > arr[j]:
            i += 1
            # i와 j사이 구간에 피봇보다 큰 값이 있다.
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    # print(f'left = {left} / right = {right} / arr = {arr}')
    return i + 1


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
