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
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
```
### 알고리즘: 병합 과정
```python
def merge(left, right):

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
- 고정된 피봇을 기준으로 좌(피봇 보다 작은 값) 우(피봇 보다 큰 값) 각각 다시 루프를 돌림
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