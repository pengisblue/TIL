# 0830 강의
## 반복(Iteration)과 재귀(Recursion)
||반복|재귀|
|:--:|:--:|:--:|
|종료|반복문의 종료 조건|재귀 함수 호출이 종료되는<br/>베이스 케이스|
|수행 시간|빠름|(상대적) 느림|
|메모리|적게 사용|(상대적) 많이 사용|
|코드 길이|길다|짧고 간결|
|코드 형태|for, while|if - else|
|무한 반복시|CPU를 반복해서 점유|스택 오버플로우|

### 재귀
```python
def f(i, N):    # i 현재 상태, N 목표
    if i == N:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, N)

N = 5
A = [1, 2, 3, 4, 5]
B = [0] * N
f(0, N)

```
```python
# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, N, key, arr):    # i 현재 상태, N 목표, key 찾고자 하는 원소
    if i == N:
        return 0    # key가 없는 경우
    elif arr[i] == key:
        return 1
    else:
        # 탐색이 끝나면 리턴값을 그냥 넘겨줄 것이기 때문에 return (function) 해줘야 함
        return f(i+1, N, key, arr)

N = 5
A = [1, 2, 3, 4, 5]
key = 10
print(f(0, N, key, A))  # 0
```
### 순열 만들기
```python
def f(i, N, K):     # i는 이전에 고른 개수, N개에서 K개를 고르는 순열
    if i == K:  # 순열 완성
        print(p)
        return
    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:    # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0


card = [1, 2, 3, 4, 5]
N = 5   # N개의 숫자에서
K = 3   # K개를 고르는 순열
used = [0] * N  # 이미 사용한 카드인지 표시
p = [0] * K
f(0, N, K)
```
```python
# 부분집합 합 구하기
a = [1, 2, 3, 4]
N = 4
# for i in range(1, (1<<N)-1):
for i in range(1, 1<<(N-1)):    # 1<<(N-1) == (1<<N)//2
    subset1 = []
    subset2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i & (i<<j):      # j번 비트가 0이 아니면
            subset1.append(a[j])
            total1 += a[j]
        else:
            subset2.append(a[j])
            total2 += a[j]
    
    # print(subset1, subset2)
    '''
    [1] [2, 3, 4]
    [1] [2, 3, 4]
    [1, 2] [3, 4]
    [1] [2, 3, 4]
    [1, 3] [2, 4]
    [1, 2] [3, 4]
    [1, 2, 3] [4]
    '''
```
```python
# idx 조사대상
# chosen 선택 대상
# 완전검색
    # 모든 N개의 원소를 다 조사했는지 판단
def perm(idx, chosen):
    if idx == N:
        tmp = []
        for i in chosen:
            tmp.append(data[i])
        result.append(tmp)
        return

    # 모든 N개의 원소를 조사했는지 판단
    for i in range(N):
        # i번째에 쓰겠다고 이전에 판정된 적이 있다면,
        # 현재 조사 대상을 i번째에 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[idx] = i     # idx번째 대상을 i번째에 둬서 사용
        perm(idx+1, chosen)
        chosen[idx] = -1


N = 6
data = '124783'
result = []
# i번째에 들어갈 수 있는 0, N-1 까지를 제외한
chosen = [-1] * N
perm(0, chosen)
print(result)
'''
[['1', '2', '4', '7', '8', '3'], 
 ['1', '2', '4', '7', '3', '8'],
 ['1', '2', '4', '8', '7', '3'],
 ['1', '2', '4', '8', '3', '7'],
 ['1', '2', '4', '3', '7', '8'], ... ]
'''
```
