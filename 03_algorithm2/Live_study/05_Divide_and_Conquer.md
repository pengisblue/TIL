# 9/18 강의
## 분할정복
### 설계 전략
- 분할(Divide): 해결할 문제를 여러개의 작은 부분으로 나눈다.<br>
(나눌 수 없을 때 까지 = 문제를 쉽게 해결할 때 까지)
- 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
- 통합(Combine): (필요하다면) 해결된 해답을 모은다.
### 거듭 제곱 문제
- 2^8 = 2^4 * 2^4
- 2^4 = 2^2 * 2^2
- 2^2 = 2 * 2
## 병합 정렬(Merge Sort)
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 알고리즘 활용
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
    - top-down 방식
- 시간복잡도: O(n log n)
### 알고리즘: 분할 과정
```python
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
```
### 알고리즘: 병합 과정
```python
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
print(merge_sort(arr))      # [2, 8, 10, 16, 22, 30, 31, 69]
'''
left: [69] / right: [10] / result: [10, 69]
left: [30] / right: [2] / result: [2, 30]
left: [10, 69] / right: [2, 30] / result: [2, 10, 30, 69]
left: [16] / right: [8] / result: [8, 16]
left: [31] / right: [22] / result: [22, 31]
left: [8, 16] / right: [22, 31] / result: [8, 16, 22, 31]
left: [2, 10, 30, 69] / right: [8, 16, 22, 31] / result: [2, 8, 10, 16, 22, 30, 31, 69
'''
```
## 퀵 정렬
- 병합 정렬과의 차이점
    - 기준 아이템(pivot item)을 중심으로 작은 것은 왼편, 큰 것은 오른편에 위치
    - 병합이란 후처리 작업이 필요하지 않음
#### Hoare-Partition 알고리즘
- 아이디어
    0. 피봇 선택
        - 배열의 시작, 중간 끝에 위치한 값 중 중간 값
    1. 피봇값 보다 큰 값은 오른쪽, 작은 값은 왼쪽 집합에 위치하도록 한다
        - [ P | P > 요소들 | P < 요소들 ]
    2. 피봇을 두 집합의 가운데에 위치시킨다
        - [ P > 요소들 | P | P < 요소들 ]
- 루프
    - 배열의 왼쪽에서 시작하는 i 는 피봇보다 큰 값을 찾는다
    - 배열의 오른쪽에서 시작하는 j 는 피봇보다 작은 값을 찾는다
    - i와 j의 위치를 바꿔준다
    - i와 j가 교차되면 j와 피봇을 교환
- 고정된 피봇을 기준으로 좌(피봇 보다 작은 값) 우(피봇 보다 큰 값) 각각 다시 루프
```python
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
print(arr)      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
left = 2 / right = 5 / arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
left = 3 / right = 2 / arr = [3, 2, 1, 6, 9, 4, 8, 7, 5]
left = 1 / right = 0 / arr = [1, 2, 3, 6, 9, 4, 8, 7, 5]
left = 2 / right = 1 / arr = [1, 2, 3, 6, 9, 4, 8, 7, 5]
left = 4 / right = 8 / arr = [1, 2, 3, 6, 9, 4, 8, 7, 5]
left = 6 / right = 5 / arr = [1, 2, 3, 6, 5, 4, 8, 7, 9]
left = 4 / right = 3 / arr = [1, 2, 3, 4, 5, 6, 8, 7, 9]
left = 5 / right = 4 / arr = [1, 2, 3, 4, 5, 6, 8, 7, 9]
left = 8 / right = 7 / arr = [1, 2, 3, 4, 5, 6, 8, 7, 9]
left = 7 / right = 6 / arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
```
#### Lomuto-Partition 알고리즘
- 아이디어
    - 0. 피봇은 맨 끝값
    - i와 j는 맨 앞에서 부터 시작
- 루프
    - 값이 피봇보다 작거나 같으면 i, j 둘 다 + 1
    - 값이 피봇보다 크면 j + 1
        - j가 피봇보다 작거나 같은 값을 만나면 i + 1 값과 스왑
    - j가 피봇에 도달하면 i + 1 값과 피봇 스왑
- 고정된 피봇을 기준으로 좌, 우 각각 다시 루프를 돌림
```python
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
print(arr)      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
left = 0 / right = 8 / arr = [3, 2, 4, 1, 5, 6, 8, 7, 9]
left = 0 / right = 3 / arr = [1, 2, 4, 3, 5, 6, 8, 7, 9]
left = 1 / right = 3 / arr = [1, 2, 3, 4, 5, 6, 8, 7, 9]
left = 5 / right = 8 / arr = [1, 2, 3, 4, 5, 6, 8, 7, 9]
left = 5 / right = 7 / arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
```
#### pythonic?
```python
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
print(quick_sort(arr))      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
left: [2, 1] / pivot: 3 / right: [4, 6, 9, 8, 7, 5]
left: [1] / pivot: 2 / right: []
left: [] / pivot: 4 / right: [6, 9, 8, 7, 5]
left: [5] / pivot: 6 / right: [9, 8, 7]
left: [8, 7] / pivot: 9 / right: []
left: [7] / pivot: 8 / right: []
'''
```
## 이진 검색
- 자료가 정렬된 상태에서
- 중앙 값과 key값 비교
    - key값 보다 작으면 왼쪽에서 다시 탐색
    - key값 보다 크면 오른쪽에서 다시 탐색
```python
# 반복문
arr = [2, 4, 7, 9, 11, 19, 23]

# 정렬되어 있다는 보장이 없다면 반드시 정렬을 먼저 수행해야함
arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr) -1

    # low > high 라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid + 1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid - 1
    
    return '데이터 없음'
```
```python
# 재귀
arr = [2, 4, 7, 9, 11, 19, 23]

# 정렬되어 있다는 보장이 없다면 반드시 정렬을 먼저 수행해야함
arr.sort()

# 함수 한 번 호출할 때 마다 low, high 변수가 바뀌어서 사용됨
def binarySearch(low, high, target):
    # 기저 조건: 언제까지 재귀호출을 반복할 것인가
    # low > high 라면 데이터를 못찾음
    if low > high:
        return -1

    mid = (low + high) // 2

    # 1. 가운데 값이 정답인 경우
    if arr[mid] == target:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch(mid + 1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid - 1, target)
```