def quick_sort(arr):
    # 분할
    if len(arr) <= 1:
        return arr
    else:
        # 분할 작업
        pivot = arr[0]
        left, right = [], []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
        
        # print(f'left: {left} / pivot: {pivot} / right: {right}')
        return [*quick_sort(left), pivot, *quick_sort(right)]
    
arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(quick_sort(arr))
