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
### 부분집합 합 문제
