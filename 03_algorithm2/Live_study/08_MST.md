# 9/21 강의
## 최소 비용
- 가중치의 합이 최소가 되는 트리: MST
- 정점 사이의 최소 비용(최단거리): 다익스트라
### 신장 트리
1. 모든 정점을 연결
2. 사이클(시작과 끝이 이어진)이 존재하지 않는 부분 그래프
    - 간선의 개수: N-1개
3. 한 그래프에서 여러개의 신장 트리가 나올 수 있다
## 최소 신장 트리 (Minimum Spanning Tree)
- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리
- 전체를 연결하며 비용이 최소(거리가 짧다)
### 접근
1. `특정 정점`에서 출발해서 갈 수 있는 곳들 중 가장 짧은 곳
    - 모든 정점을 방문할 때 까지
    - BFS + 가중치 활용
2. `전체 간선`들 중에서 제일 가중치가 적은 곳 부터 선택
    - 간선 정보 `정렬`
    - 기존 방문 여부 확인
### 구현
```python
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
```
#### Prim  알고리즘
> 1. `특정 정점`에서 출발해서 갈 수 있는 곳들 중 가장 짧은 곳
```python
import heapq


def prim(start):
    heap = []
    MST = [0] * V   # MST에 포함되었는지 여부(visited)
    heapq.heappush(heap, (0, start))    # 가중치, 정점 정보
    sum_weight = 0  # 누적합 저장

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        if MST[v]:  # 이미 방문한 노드라면 pass
            continue
        MST[v] = 1  #방문 체크
        sum_weight += weight    # 누적합 추가
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]     # 인접행렬
for _ in range(E):
    f, t, w = map(int, input().split())
    # 무방향 그래프
    graph[f][t] = w
    graph[t][f] = w

result = prim(0)
print(f'최소비용 = {result}')   # 최소비용 = 175
```
#### KRUSKAL 알고리즘
> 2. `전체 간선`들 중에서 제일 가중치가 적은 곳 부터 선택
```python
V, E = map(int, input().split())
edge  = []  
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])

# 사이클 발생 여부를 union find로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:  # 사이클 발생
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 사이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST구성이 끝나면
        if cnt == V:
            break

print(f'최소비용 = {sum_weight}')   # 최소비용 = 175
```
## 최단 경로
- 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단 경로
    - 다익스트라(dijkstra) 알고리즘
        - 음의 가중치를 허용하지 않음
    - 벨만-포드(Bellman-Ford) 알고리즘
        - 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
    - 플로이드-워샬(Floyd-Warshall) 알고리즘
### 유형
- 특정지점 -> 도착 지점까지의 최단 거리: 다익스트라
- 가중치에 음수가 포함: 벨만포드
- 여러지점 -> 여러지점까지의 최단 거리:
    - 여러 지점 모두 다익스트라 -> 시간 복잡도 계산 잘 해야함
    - 플로이드-워샬
### Dijkstra 알고리즘
```python
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
```
```python
# 내가 갈 수 있는 경로 중 누적 거리가 제일 짧은 것 부터 고르기
import heapq

# 입력
n, m = map(int, input().split())
# 인접리스트
graph = [[] for _ in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 1. 누적 거리를 계속 저장
INF = int(1e9)  # 최대값으로 1억 - 대충 엄청 큰 수
distance = [INF] * n

def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크다?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dijkstra(0)
print(distance)     # [0, 2, 3, 9, 6, 10]
```