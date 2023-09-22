# 9/20 강의
## 그래프
- 데이터 간 관계를 표현한 자료구조
    - 관계: 데이터 사이의 연관성
### 인접행렬
- 장점: 구현이 쉽다
- 단점: 메모리 문제 (0도 기록하기 때문에)
```python
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
]
```
### 인접리스트
```python
# 각 노드마다 갈 수 있는 지점의 개수가 다름
# 메모리적으로 인접 행렬에 비해 효율적이다.
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]
'''
파이썬은 딕셔너리로도 구현할 수 있다
graph = {
    '0': [1, 3],
    '1': [0, 2, 3, 4],
    '2': [1],
    '3': [0, 1, 4],
    '4': [1, 3]
}
'''
```

## DFS
### stack
```python
def dfs_stack(start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue
        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)
        # 갈 수 있는 곳들을 stack에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue
            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited


print(*dfs_stack(0))    # 0 3 4 1 2
```
### 재귀
```python
visited = [0] * 5
path = []

def dfs(now):
    visited[now] = 1    # 현재 지점 방문 표시
    print(now, end=' ')

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue
        
        if visited[next]:
            continue
        
        def(next)


dfs(0)  # 0 1 2 3 4
```
## BFS
```python
from collections import deque
def bfs(start):
    visited = [0] * 5

    # 먼저 방문 했던 것을 먼저 처리해한다
    queue = deque([start])
    visited[start] = 1

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        # 인접한 노드들을 queue에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue
            # 방문한 지점이라면 queue에 추가하지 않음
            if visited[next]:
                continue

            queue.append(next)
            visited[next] = 1


bfs(0)  # 0 1 3 2 4
```
## 서로소 집합들
### 서로소 집합(Disjoint-sets), 상호배타 집합
- 교집합이 없는 집합들
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다
    - 대표자(representative)
#### 상호배타 집합 연산
- Make-Set(x)
- Find-Set(x): 각 요소가 내가 속한 그룹의 대표자를 어떻게 찾을 지
- Union(x,y): 대표자 저장(같은 그룹으로 묶기)  
#### 표현 방법
- 연결 리스트
- 트리
```python
# 트리를 이용한 표현
# 0 ~ 9
# make-set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find-set
def find_set(x):
    if parent[x] == x:
        return x
    
    return find_set(parent[x])

# union
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    # 2. 대표자가 같으면 같은 집합
    if x == y:
        print('사이클 발생')
        return

    # 3. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


union(0, 1)
union(2, 3)
# 대표자 검색
print(find_set(2))  # 2
print(find_set(3))  # 2

union(1, 3)
print(find_set(2))  # 0
print(find_set(3))  # 0

union(0, 2)     # 싸이클 발생

# 같은 그룹인지 판별
if find_set(0) == find_set(2):
    print('같은 집합')
else:
    print('다른 집합')
# 같은 집합
```
#### 연산의 효율 높이기
```python
# Path compression
def find_set(x):
    if parent[x] == x:
        return x
    
    # return find_set(parent[x])

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]
```
```python
# Rank를 이용한 union
```