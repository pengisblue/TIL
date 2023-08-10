# 7/31 강의

## 알고리즘
### 시간 복잡도(Time Complexity)
- 빅-오(O) 표기법

## 배열
> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
- 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.
### 1차원 배열
#### 선언
- arr = list()
- arr = []
- arr = [1, 2, 3]
- arr = [0] * 10
#### 접근
- arr[idx] = 20

#### 예제: Gravity
- solve
    - arr[i] 다음에 오는 수 중에 자신보다 큰 수의 개수 == 낙하 높이

## 정렬
### 버블 정렬 (Bubble Sort)
- 인접한 두 개의 원소를 비교하여 자리를 계속 교환하는 방식
#### [55, 7, 78, 12, 42]를 버블 정렬 (오름차순)
##### 첫 번째 (가장 큰 수를 맨 뒤로)
| _55_ | _07_ | 78 | 12 | 42 | <br/>
| 07 | _55_ | _78_ | 12 | 42 | <br/>
| 07 | 55 | _78_ | _12_ | 42 | <br/>
| 07 | 55 | 12 | _78_ | _42_ | <br/>
| 07 | 55 | 12 | 42 | **_78_** | <br/>

##### 두 번째 (다음 큰 수)
| _07_ | _55_ | 12 | 42 | 78 | <br/>
| 07 | _55_ | _12_ | 42 | 78 | <br/>
| 07 | 12 | _55_ | _42_ | 78 | <br/>
| 07 | 12 | 42 | **_55_** | **_78_** | <br/>
 
(...)

```python
for i: N - 1 -> 1
    for j: 0 -> i - 1
        if A[j] + A[j + 1]:
            A[j] <-> A[j + 1]
```
```python
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                # tmp = a[j]
                # a[j] = a[j+1]
                # a[j+1] = tmp
                a[j], a[j+1] = a[j+1], a[j]
```

# 8/1 강의

## 정렬
### 카운팅 정렬 (Counting Sort)
> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, <br/>선형 시간에 정렬하는 효율적인 알고리즘

- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능

1. Data에서 각 항목들의 발생 회수를 세고, 정수 학목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다.

    ```python
    Data = [0, 4, 1, 3, 1, 2, 4, 1]
    max_v = max(Data)
    counts = [0] * (max_v+1)
    for x in Data:
        counts[Data] += 1
    # counts = [1, 3, 1, 1, 2]
    ```
2. 각 항목의 누적값으로 counts를 조정한다
    ```python
    for i 1 -> 4:
        counts[i] += count[i-1]
    # counts = [1, 4, 5, 6, 8]
    ```
3. Data의 뒤 부터 탐색
    ```python
    temp = [0] * len(Data)
    for j N-1 -> 0:
        counts[Data[j]] -= 1
        temp[counts[Jata[j]]] = Data[j]
    # temp = [0, 1, 1, 1, 2, 3, 4, 4]
    ```
```python
# 매개변수가 2개 필요하다.
# 입력 배열 : numbers
# numbers가 가진 최대 정수 값 : k
def counting_sort(numbers, k):
    '''
    카운트 배열 : count_arr : k+1 번 인덱스까지
    '''
    count_arr = [0] * (k+1)
    # print(count_arr)
    # for i in range(k+1):
    #     count_arr.append(0)
    # 최종 정렬 된 값을 담을 배열
    # result의 범위 : numbers의 전체 원소 양 만큼
    result = [-1] * len(numbers)

    for i in range(len(numbers)):
        count_arr[numbers[i]] += 1
    # print(count_arr)

    # 각 요소가 들어있는 개수를 확인했으니...
    # 각 요소가 들어가야 할 인덱스를 계산하기 위해
    # 누적 값 카운팅
    for i in range(1, len(count_arr)):
        # print(count_arr[i], count_arr[i - 1])
        count_arr[i] += count_arr[i - 1]
    # print(count_arr)
    # 원본 배열의 값들을 다시 순회하면서
    # 원본 배열의 각 값들을 정렬 된 인덱스 위치에 담아주기
    for num in numbers:
        count_arr[num] -= 1
        result[count_arr[num]] = num
    return result


numbers = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(numbers, 5))
```

```python
def counting_sort(A, B, K):
    # A[] : 입력 배열(0 to k)
    # B[] : 정렬된 배열
    # C[] : 카운트 배열

    C = [0] * (k+1)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1,len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```

## Baby-gin Game
> - 0~9 사이의 숫자 카드에서 임의로 6장을 뽑았을 때,
>   - 3장이 연속적인 번호: run
>   - 3장이 동일한 번호: triplet
> - 6장이 run과 triplet로만 구성된 경우 baby-gin
> - 6자리 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라

### 완전 검색을 활용한 접근
- 고려할 수 있는 모든 경우의 수 생성하기: 순열
### 탐욕 알고리즘
1. 해 선택
2. 실행 가능성 검사
3. 해 검사
```python
num = 456789  # Baby Gin 확인할 6자리 수
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:  # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[1+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2: print('Baby Gin')
else: print('Lose')
```