def hoare_partition(left, right):
    pivot = arr[left]
    left += 1

    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        # print(f'left = {left} / right = {right} / arr = {arr}')

        # 엇갈린 경우 right 가 pivot 의 위치
        if left >= right:
            return right

        arr[left], arr[right] = arr[right], arr[left]

def quick_sort(left, right):
    # left 가 right 보다 커지면 종료
    if left >= right:
        return

    pivot = hoare_partition(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]

    quick_sort(left, pivot)
    quick_sort(pivot + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
print(arr)
