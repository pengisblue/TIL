# 8/3 강의

## 배열 2
### 2차원 배열
- arr[행][열]
- arr = [[0, 1, 2, 3], [4, 5, 6, 7]] (2행 4열의 2차원 list)
```python
# 참고
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
print(arr)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = int(input())
arr = [list(map(int, input())) for i in range(N)]
print(arr)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
#### 배열 순회
1. 행 우선 순회
```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(Array[i][j])  # 필요한 연산 수행
```
2. 열 우선 순회
```python
# i 행의 좌표
# j 열의 좌표
for j in range(m):
    for i in range(n):
        f(Array[i][j])  # 필요한 연산 수행
```
3. 지그재그 순회
```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(Array[i][j + (m-1-2*j) * (i%2)])  # i%2 -> 0 or 1 / j + (m-1-2*j) = m-1-j
        # 짝수면 j, 홀수면 m-1-j
```
- 
    ```python
    Array = [[0, 1, 2, 3] for i in range(3)]
    n, m = 3, 4

    for i in range(n):
        for j in range(m):
            print(Array[i][j], end=' ')
        print()
        '''
        0 1 2 3 
        0 1 2 3 
        0 1 2 3
        '''

    for i in range(n):
        for j in range(m):
            print(Array[i][j + (m-1-2*j) * (i%2)], end=' ')
        print()
        '''
        0 1 2 3
        3 2 1 0
        0 1 2 3
        '''
    ```
```python
N = 2  # 행의 크기
M = 4  # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
    '''
    0 1 2 3 
    4 5 6 7 
    '''

for j in range(M):
    for i in range(N):
        print(arr[i][j], end=' ')
    print()
    '''
    0 4
    1 5
    2 6
    3 7
    '''

for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i%2)], end=' ')
    print()
    '''
    0 1 2 3
    7 6 5 4
    '''

for i in range(N):
    for j in range(M):
        if i % 2:  # 행이 홀수인 경우
            print(arr[i][M-1-j], end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
    '''
    0 1 2 3
    7 6 5 4
    '''
```
#### 0으로 채워진 2차원 배열
```python
N, M = 2, 4
arr = [[0]*M for i in range(N)]
arr[0][0] = 1
print(arr)  # [[1, 0, 0, 0], [0, 0, 0, 0]]
# arr2 = [[0] * M] * N  # 쓰면 안됨
# arr2[0][0] = 1
# print(arr2)  # [[1, 0, 0, 0], [1, 0, 0, 0]]
```

#### 델타를 이용한 2차원 배열 탐색
||||
|:--:|:--:|:--:|
||( i-1, j+0 )||
|( i+0, j-1 )|( i, j )|( i+0, j+1 )|
||( i+1, j+0 )||
```python
arr[0...N-1][0...N-1]  # NxN 배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:  # 유효한 인덱스면
                f(arr[ni][nl])
```
- ```python
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    '''
    3
    1 2 3
    4 5 6
    7 8 9
    '''
    max_v = 0  # 모든 원소가 0이상
    for i in range(N):  # 모든 원소 arr[i][j]에 대해
        for j in range(N):
            # arr[i][j]중심으로
            s = arr[i][j]
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0<=ni<N and 0<=nj<N:  # 배열을 멋어나지 않으면
                    s += arr[ni][nj]
            # 여기까지 주변 원소를 포함한 합
            if max_v < s:
                max_v = s
    ```
- ```python
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    '''
    3
    1 2 3
    4 5 6
    7 8 9
    '''
    max_v = 0  # 모든 원소가 0이상
    for i in range(N):  # 모든 원소 arr[i][j]에 대해
        for j in range(N):
            # arr[i][j]중심으로
            s = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N:  # 배열을 멋어나지 않으면
                    s += arr[ni][nj]
            # 여기까지 주변 원소를 포함한 합
            if max_v < s:
                max_v = s
    ```
- ```python
    # 여러칸 탐색
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    m = int(input())
    '''
    3
    1 2 3
    4 5 6
    7 8 9
    '''
    max_v = 0  # 모든 원소가 0이상
    for i in range(N):  # 모든 원소 arr[i][j]에 대해
        for j in range(N):
            # arr[i][j]중심으로
            s = arr[i][j]
            for k in range(4):
                for p in range(1, m):
                    ni, nj = i+di[k]*p, j+dj[k]*p
                    if 0<=ni<N and 0<=nj<N:  # 배열을 멋어나지 않으면
                        s += arr[ni][nj]
            # 여기까지 주변 원소를 포함한 합
            if max_v < s:
                max_v = s
    ```
#### 전치행렬
> 대각선 중심으로 양쪽 변화
```python
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
'''
3
1 2 3
4 5 6
7 8 9
'''
for i in range(3):
    for j in range(i+1, 3):
        if i < j:  # 조건이 없으면 원래대로 돌아감
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]  # arr[i][j]<->arr[j][i]
print(arr)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

# 8/4 강의
## 비트연산자
- & : 비트 단위로 and 연산을 한다
- | : 비트 단위로 or 연산을 한다
- << : 피연산자의 비트 열을 왼쪽으로 이동 시킨다
- \>> : 피연산자의 비트 열을 오른쪽으로 이동 시킨다 

### << 연산자
- 1 << n : 2^n
    - 1 << 3 == 1000 (1을 3번 옮김) 1000(2) = 2^3
### & 연산자
- i & (1 << j): i의 j번째 비트가 1인지 아닌지를 검사한다
### 모든 부분집합 구하기
```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=', ')
    print()
print()
```

## 검색 search
### 순차 검색(Sequential Search)
- 순서대로 검색
- 구현이 쉽지만 검색 대상이 많아지면 수행시간 증가
    - 비효율적
### 이진 검색(Binary Search)
> 자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 정하고 검색을 계속 진행
1. 자료의 중앙에 있는 원소를 고른다
2. 중앙 원소 값과 목표 값을 비교한다
3. 목표 값이 중앙 원소 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색,<br/>
    크다면 자료의 오른쪽 반에 대해서 새로 검색
4. 찾고자 하는 값을 찾을 때 까지 반복
    ```python
    def binarySearch(a, N, key):
        start = 0
        end = N - 1
        while start <= end:
            middle = (start + end)//2
            if a[middle] == key:
                return true
            elif a[middle] > key:
                end = middle - 1
            else:
                start = middle + 1
        return false
    ```
```python
# arr: 원본 배열
# N: 배열의 길이
# key: 타겟
def binary_search(arr, N, key):
    start = 0
    end = N-1  # 끝 인덱스
    while start <= end:  # 시작지점이 끝지점보다 작거나 같은 동안
        mid = (start + end) // 2 # 중앙 인덱스
        # 중앙 위치가 내가 찾는 대상이라면
        if arr[mid] == key:
            return True
        # 아닌데, 중앙 위치 값이 내 키 값보다 크면
        elif arr[mid] > key:
            end = mid -1
        # 아닌데, 중앙 위치 값이 내 키 값보다 작으면
        else:
            start = mid + 1
    return False
```
### 선택 정렬(Selection Sort)
> 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 비교하는 방식
```python
def selectionSort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
```