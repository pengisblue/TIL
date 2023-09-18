def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    left, right = [], []
    mid = len(arr) // 2
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, len(arr)):
        right.append(arr[i])
        
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    # print(f'left: {left} / right: {right}', end=' / ')

    while left or right:
        if left and right:
            if  left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # print(f'result: {result}')
    return result


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(arr))
