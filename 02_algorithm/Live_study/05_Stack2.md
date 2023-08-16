# 8/14 강의
## 계산기 1
> 스택을 이용하여 계산식의 값을 계산할 수 있다.
1. 중위 표기법의 수식을 후위 표기법을 변경한다.
2. 후위 표기법의 수식을 스택을 이용하여 계산한다.
    - 중위표기법(infix notation)
        - 연산자를 피연산자 가운데 표기하는 방법 (A+B)
    - 후휘표기법(postfix notation)
        - 연산자를 피연산자 뒤에 표기하는 방법 (AB+)
### 중위표기식의 후위표기식 변환
( 6 + 5 * ( 2 - 8 ) / 2 )
- 토큰이 여는 괄호 : push
- 피연산자(숫자)는 출력
- 연산자는 우선순위가 높으면 push 
- 같거나 낮으면 stack 안의 연산자가 낮은 연산자 일 때 까지 pop()
    - stack 안에서는 여는 괄호 < +,- < *,/
    - stack 밖에서는 +,- < *,/ < 여는 괄호
- 닫는 괄호를 만나면 여는괄호가 나올 때 까지 pop(), 여는 괄호 버림
- 결과 : 6528-*2/+
```python
# (6+5*(2-8)/2)
stack = [0] * 100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}   # 스택 밖 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}   # 스택 안 우선순위

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':   # 피연산자
        susik += x
    elif x == ')':      # '('까지 pop()
        while stack[top] != '(':    # peek
            susik += stack[top]
            top -= 1
        top -= 1    # '(' 버림 pop()
    else:       # '(+-*/'
        if top == -1 or isp[stack[top]] < icp[x]:   # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1    # push
            stack[top] = x

print(susik)    # 6528-*2/+
```

## 계산기 2
### 후위 표기법의 수식을 스택을 이용하여 계산
- 피연산자를 만나면 스택에 push
- 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop()하여 연산하고 (먼저 꺼낸 숫자가 뒤로 감)
- 연산결과를 다시 스택에 push
- 수식이 끝나면 마지막으로 스택을 pop하여 출력
```python
# 6528-*2/+
stack = [0]*100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*':     # 피연산자이면
        top += 1    # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]    # pop()
        top -= 1
        op1 = stack[top]    # pop()
        top -= 1
        if x == '+':    # op1 + op2
            top += 1    # push()
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])   # -9.0
```
# 8/16 강의
##  재귀 연습
### 재귀를 이용하여 배열 복사하기
```python
def f(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        f(i+1, N)
        return
    

N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)
print(B)    # [1, 2, 3]
```
### 부분집합 재귀
```python
def f(i, N):
    if i == N:
        print(bit, end=' ')
        for j in range(N):
            if bit[j]:  # 비트의 원소가 1이면
                print(A[j], end=' ')
        print()
        return
    else:
         bit[i] = 1
         f(i+1, N)
         bit[i] = 0
         f(i+1, N)
         return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3)

'''
[1, 1, 1] 1 2 3 
[1, 1, 0] 1 2 
[1, 0, 1] 1 3
[1, 0, 0] 1
[0, 1, 1] 2 3
[0, 1, 0] 2
[0, 0, 1] 3
[0, 0, 0]
'''
```
### 부분집합의 합 구하기
```python
def f(i, N):
    if i == N:
        print(bit, end=' ')
        s = 0   # 부분집합의 합
        for j in range(N):
            if bit[j]:  # 비트의 원소가 1이면
                s += A[j]
                print(A[j], end=' ')
        print(f' : {s}')
        return
    else:
         bit[i] = 1
         f(i+1, N)
         bit[i] = 0
         f(i+1, N)
         return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3)

'''
[1, 1, 1] 1 2 3  : 6
[1, 1, 0] 1 2  : 3
[1, 0, 1] 1 3  : 4
[1, 0, 0] 1  : 1
[0, 1, 1] 2 3  : 5
[0, 1, 0] 2  : 2
[0, 0, 1] 3  : 3
[0, 0, 0]  : 0
'''
```
### 부분집합의 합 구하기 2
```python
def f(i, N, s):     # s: i-1원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end=' ')
        print(f' : {s}')
        return
    else:
         bit[i] = 1     # 부분집합에 A[i] 포함
         f(i+1, N, s+A[i])
         bit[i] = 0
         f(i+1, N, s)   # 부분잡합에 A[i] 빠짐
         return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3, 0)

'''
[1, 1, 1]  : 6
[1, 1, 0]  : 3
[1, 0, 1]  : 4
[1, 0, 0]  : 1
[0, 1, 1]  : 5
[0, 1, 0]  : 2
[0, 0, 1]  : 3
[0, 0, 0]  : 0
'''
```
### 부분집합의 합이 10인 경우
```python
def f(i, N, s):     # s: i-1원소까지 부분집합의 합(포함된 원소의 합)
    global cnt
    cnt += 1
    if i == N:
        if s == 10:
            print(bit)
        return
    else:
         bit[i] = 1     # 부분집합에 A[i] 포함
         f(i+1, N, s+A[i])
         bit[i] = 0
         f(i+1, N, s)   # 부분잡합에 A[i] 빠짐
         return


# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0)
print(cnt)  # 1701

'''
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
[1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
'''
```
## 백트래킹
- 해를 찾는 도중에 막히면 (해가 아니면) 되돌아가서 다시 해를 찾는 기법
### 백트래킹과 깊이우선탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 그 경로의 탐색을 멈춤(가지치기)
- 깊이 우선탐색은 모든 경로를 추적, 백트래킹은 불필요한 경로를 조기에 차단(모든 후보 검사 x)

```python 
def checknode(v):   # node
    if promising(v):
        if there is a solution at(v):
            write the solution
        else: for u in each child of v:
            checknode(u)
```
### 부분집합의 합
```python
def f(i, N, s, t):     # s: i-1원소까지 부분집합의 합(포함된 원소의 합), t 찾으려는 합
    global cnt
    cnt += 1
    if s == t:      # 목표치를 찾은 경우
        print(bit)
        return
    elif i == N:    # 모든 원소에 대한 고려가 끝난 경우
        return
    elif s > t:     # 남은 원소를 고려할 필요가 없는 경우
        return
    else:
         bit[i] = 1     # 부분집합에 A[i] 포함
         f(i+1, N, s+A[i], t)
         bit[i] = 0
         f(i+1, N, s, t)   # 부분잡합에 A[i] 빠짐
         return


# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print(cnt)  # 349 <- 시행횟수 감소
'''
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
[1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
'''
```
```python
def solution(arr, end, result):
    # 부분집합의 합이 10인 경우
    if result != 10:
        return
    for i in range(1, end+1):
        if arr[i]:
            print(data[i], end=' ')
    print()


def construct_candidates(c):
    c[0] = True     # 쓴다
    c[1] = False    # 안쓴다
    return c


# 체크할 배열
# 시작점 (현재 조사 위치)
# 종료지점 (모든 원소의 개수가 종료시점 == N)
# 총합: 누적값 acc
def backtracking(arr, now, end, result):
    global cnt
    if result > 10:
        return
    cnt += 1
    # 후보군 목록
    # 부분집합의 원소로 now 번째의 값을 T/F (쓴다/안쓴다)
    c = [0] * 2
    # 언제까지 조사할 것이냐
    if now == end:
        solution(arr, end, result)    # 값을 도출하는 함수를 호출
    else:
        # print(now, result, arr)
        # 아직 조사해야하는 원소가 남았다
        # 다음 원소를 조사 하러 가기 위해 index 1 증가
        now += 1
        # now가 1 증가된 다음
        # 내가 arr[now] 값을 쓸지 말지를 판별할 수 있는 후보군 만들기
        # arr, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 목록
        ncandidates = construct_candidates(c)
        # 후보군 수 만큼 반복해서 조사
        for i in range(len(ncandidates)):
            arr[now] = c[i]
            if arr[now]:    # 현재 조사하고 있는 대상 쓰기로 했으면
                # now번째 원소 쓰기로 했으면
                # 부분집합의 합의 누적 값이 now번째 원소의 값 만큼 증가
                backtracking(arr, now, end, result + data[now])
            else:
                # now번째 원소를 안썼을 때
                backtracking(arr, now, end, result)

# 유망성: 다음 조사를 하는 의미
# 후보군 수: 우리의 후보군이란, 0 1 (안쓰거나 쓰거나)
# MAXCANDIDATES = 2
# 최대 원소 개수
NMAX = 12
cnt = 0

data = list(range(11))
arr = [0] * NMAX    # 각 원소를 사용할 것이냐 말 것이냐를 체크할 배열
# [1, 2, 3, 4]
# [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
backtracking(arr, 0, 10, 0)
print(cnt)
```
```python
def powerset(arr, now, result):
    if sum(result) > 10:
        return

    if now == len(arr):
        if sum(result) == 10:
            print(result)
        return
    powerset(arr, now + 1, result + [arr[now]])
    powerset(arr, now + 1, result)
arr = list(range(1, 11))
powerset(arr, 0, [])
```
```python
# 비트계산 복습
arr = list(range(1, 11))# 1~10
n = len(arr)    # 길이가 10인 경우의 모든 경우의 수
# 2 ** n
# 1 << n
for i in range(1 << n):
    # 모든 경우의 수 에 대해서
    # 만들 수 있는 부분집합
    subset = []
    for j in range(n):
        # i번째 경우의 수 일 떄,
        # j번째 요소를 쓰는가
        if i & (1 << j):
            subset.append(arr[j])
    # 부분집합의 합이 10 이냐
    if sum(subset) == 10:
        print(subset)
```
## 순열
```python
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):   # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]     # 원상복구


A = [0, 1, 2]
f(0, 3)
'''
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[1, 2, 0]
[2, 1, 0]
[2, 0, 1]
'''
```
## 분할 정복 알고리즘
### 거듭제곱
- 2 ** 8 계산
    - 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
    - ((2²)²)² 와 같은 방식으로 분할
```python
# 분할 정복을 사용하지 않은 거듭제곱
def f1(b, e):
    global cnt1
    if b == 0:
        return 1
    r = 1
    for i in range(e):
        cnt1 += 1
        r *= b
    return r


# 분할 정복을 사용한 거듭제곱
def f2(b, e):
    global cnt2
    if b == 0 or e == 0:
        return 1
    if e % 2:   # 거듭제곱 횟수가 홀수이면
        r = f2(b, (e-1)//2)
        cnt2 += 1
        return r*r*b
    else:
        r = f2(b, e//2)
        cnt2 += 1
        return r*r
    

cnt1 = 0
cnt2 = 0
print(f1(2, 20), cnt1)  # 1048576 20
print(f2(2, 20), cnt2)  # 1048576 5
```