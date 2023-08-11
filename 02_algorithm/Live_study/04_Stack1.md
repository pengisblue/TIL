# 8/9 강의

## 스택
### 특성
1. 선형 구조
    - 자료 간의 1대 1의 관계
2. `후입선출(LIFO, Last-In-First-Out)`

### 자료구조와 연산
- 자료구조: 자료를 선형으로 저장할 저장소
    - top - 스택에서 마지막 삽입된 원소의 위치
- 연산
    - push: 삽입
    - pop: 삽입한 자료의 역순으로 꺼낸다
    - isEmpty
    - peek: 스택의 top에 있는 원소를 반환하는 연산

### 구현
```python
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow')   # 디버깅 목적
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20     # push(20)
```
```python
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]
    
print(pop())

if top > -1:    # pop()
    top -= 1
    print(stack[top+1])
```
```python
stack = [0] * 10
top = -1

top += 1
stack[top] = 1      # push(1)
top += 1
stack[top] = 2      # push(2)
top += 1
stack[top] = 3      # push(3)

print(stack[top])   # pop() 3
top -= 1
top -= 1
print(stack[top+1]) # pop() 2

```

## 재귀호출

## Memoization
- 이전에 계산한 값을 메모리에 저장해서 실행 속도를 빠르게 하는 기술
```python
# memoization을 활용한 피보나치 수열
# memo를 위한 배열을 할당, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]는 1로 초기화

def fibo(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo(n-1) + fibo(n-2))
    return memo[n]

n = 10
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
```

# 8/10 강의

## DP(Dynamic Programming)
> 동적 계획 알고리즘
1. 문제를 부분 문제로 분할
2. 가장 작은 부분 문제부터 해를 구한다
3. 그 결과는 테이블에 저장
4. 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.
```python
def fibo(n):
    df = [0] * (n + 1)
    df[0] = 0
    df[1] = 1
    for i in range(2, n + 1):
        df[i] = df[i-1] + df[i-2]
    
    return df[n]
```

## DFS(깊이우선탐색)
> 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가<br/>
더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길이 있는 정점으로 되돌아와서<br/>
다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

> 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서<br/> 
다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
1. 시작 정점 v를 결정하여 방문한다
2. 정점 v에 인접한 정점 중에서
    - 방문하지 않은 `정점 w가 있으면`, 
        - `정점 v`를 스택에 `push` 정점 w 방문
        - `w를 다시 v로` 하여 다시 반복
    - 방문하지 않은 정점이 `없으면`,
        - 탐색의 방향을 바꾸기 위해서 `스택을 pop`하여 
        - `가장 마지막 방문 정점을 v로` 하여 다시 반복 <- 후입 선출
```python
visited[], stack[] 초기화
DFS(v)
    시작점 v 방문
    visited[v] <- True
    while:
        if v의 인접 정점 중 방문 안 한 정점 w가 있으면:
            push(v)
            v <- w (w에 방문)
            visited[w] <- True
        else:
            if 스택이 비어있지 않으면:
                v <- pop(stack)
            else:
                break
end DFS()
```
```python
'''
V E
v1 w1 v2 w2 ...
7 8     정점의 개수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7     엣지의 개수
'''
def dfs(n, V, adj_m):
    stack = []  # stack 생성
    visited = [0] * (V+1)   # visited 생성
    visited[n] = 1  # 시작점 방문 표시
    print(n, end=' ')    # do[n]
    while True:
        for w in range(1, V+1):   # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)     # push(v), v = w
                n = w
                print(n, end=' ')    # do(w)
                visited[n] = 1  # w 방문 표시
                break   # for w, n에 인접인 w 찾은 경우
        else:
            if stack:   # 스택에 지나온 정점이 남아있으면
                n = stack.pop()     # pop()해서 다시 다른 w를 찾을 n 준비
            else:   # 스택이 비어있으면
                break   # while 탐색 끝

V, E = map(int, input().split())    # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
print(adj_m)
dfs(1, V, adj_m)    # 1 2 4 6 5 7 3
```
```python
'''
V E
v1 w1 v2 w2 ...
7 8     정점의 개수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7     엣지의 개수
'''
def dfs(node):      # 노드 번호를 받아서 해당 노드부터 조사를 시작
    stack = [node]      # stack을 활용
    # stack.append(node)
    visited = [False] * (V+1)   # 조사 여부 체크용 리스트
    while stack:    # stack에 (조사해야할) 값dl dlTsms ehddks
        start = stack.pop()     
        if visited[start] == 0:     # 이전에 방문한 적이 없다면
            visited[start] = True   # 방문했다
            print(start, end=' ')
            for next in range(0, V+1):
                if matrix[start][next] == 1 and visited[next] == 0:
                    stack.append(next)


V, E = map(int, input().split())    # node의 개수, Edge 간선의 개수
data = list(map(int, input().split()))      # 간선 정보

matrix = [[0]*(V+1) for _ in range(V+1)]    # 이동 가능 정보 2차원 리스트

# for i in range(E):
#     print(data[i * 2], data[i * 2 + 1])
for i in range(0, E*2, 2):      # 모든 간선 순회
    # print(i, i+1, data[i], data[i+1])
    matrix[data[i]][data[i+1]] = 1
    matrix[data[i+1]][data[i]] = 1      # 양방향 이동 이므로

dfs(1)      # 1 3 7 6 5 2 4
```
```python
# recur
# 노드 번호를 받아서 해당 노드부터 조사를 시작
def DFS(node):
    visited[node] = True  # 방문 했다.

    print(node, end=' ')
    for next in range(1, V + 1):
        # 다음 조사 가능 여부
        if matrix[node][next] == 1 and visited[next] == 0:
            DFS(next)
        # else -> 이전 DFS(node)로 돌아감

# V = node의 개수
# E = Edge 간선의 개수
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))
visited = [False] * (V + 1)  # 노드가 7개인데, 7번 인덱스까지 필요하니까 7+1 개의 값을 가진 리스트
# 이동 가능 정보 2차원 리스트
matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 모든 간선 순회
# for i in range(E):
#     print(data[i * 2], data[i * 2 + 1])
for i in range(0, E * 2, 2):
    # print(i, i+1, data[i], data[i+1])
    matrix[data[i]][data[i + 1]] = 1
    matrix[data[i + 1]][data[i]] = 1

DFS(1)  # 1 2 4 6 5 7 3
```