# 8/17 강의
## 큐 (Queue)
- 스택과 같이 삽입과 삭제의 위치가 제한적인 자료구조
- 뒤에서는 삽입만 하고 앞에서는 삭제만 이루어지는 구조(선입선출: FIFO)
- 머리(Front) : 삭제, 꼬리(Rear) : 삽입
### 기본 연산
삽입: enQueue(item)
삭제: deQueue()
공백큐 생성: createQueue()
공백 확인: isEmpty()
포화 확인: isFull()
앞쪽 원소 반환: Qpeek()

### 선형큐
- 1차원 배열을 이용한 큐
- 표현
    - 초기 상태: front = rear = -1
    - 공백 상태: front == rear
    - 포화 상태: rear == n-1 (n: 배열의 크기)
#### 구현
```python
def enQ(data):
    global rear
    if rear == Qsize-1:     # 포화 상태면
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data


def deQ():
    global front
    if front == rear:   # 비어있으면
        print('큐가 비어있음')
        return -1
    else:
        front += 1
        return Q[front]


Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

enQ(1)
enQ(2)
rear += 1   # enqueu(3)
Q[rear] = 3
# enQ(4)  # Q is Full

# while front != rear:
#     front += 1
#     print(Q[front])

print(deQ())    # 1
print(deQ())    # 2
print(deQ())    # 3
print(deQ())    # 큐가 비어있음
                # -1
```
### 원형큐
- 초기 공백
    - front = rear = 0
- index의 순환
    - mod 연산자 사용
- 삽입, 삭제 위치

||삽입 위치|삭제위치|
|:--:|:--:|:--:|
|선형큐|rear = rear + 1|front = front + 1|
|원형큐|rear = (rear+1) % n|front = (front+1) % n|
- 표현
    - 공백: front == rear
    - 포화: (rear + 1) % n == front (삽입할 rear의 다음 위치 == 현재 front)

```python
def enq(data):
    global rear
    global front
    if (rear+1) % cQsize == front:
        # 포화상태이면 맨 앞에 있는 값에 덮어 씌우는 경우기로 정의
        front = (front+1) % cQsize
    rear = (rear+1) % cQsize
    cQ[rear] = data
    print(cQ)


def deq():
    global front
    if front == rear:
        return 'cQ is empty', cQ
    else:
        front = (front+1) % cQsize
        return cQ[front]

cQsize = 5
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)  # [0, 1, 0, 0]
enq(2)  # [0, 1, 2, 0]
enq(3)  # [0, 1, 2, 3]
enq(4)  # [4, 1, 2, 3]
enq(5)  # [4, 5, 2, 3]
print(deq())    # 3
print(deq())    # 4
print(deq())    # 5
print(deq())    # ('cQ is empty', [4, 5, 2, 3])
# front가 있는 자리는 사용하지 않고 비어있는 자리이기 때문에
```
### 우선순위 큐
- 우선순위를 가진 항목들을 저장하는 큐
- 배열을 사용하므로 삽입이나 삭제 연산이 일어날 때 원소 재배치에 소요되는 시간이나 메모리 낭비가 큼

# 8/18 강의
## BFS
- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에,<br/>
방문했던 정점을 시작으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, <br/>선입선출 형태의 큐를 활용
```python
def BFS(G, v, n):   # 그래프 G, 탐색 시작점 v
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in G[t]:  # t와 연결된 모든 정점에 대해
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
```

# resume
## 큐(Queue)
- 삽입과 삭제의 위치가 제한적인 자료구조로 뒤에서는 삽입만 하고, 앞에서는 삭제만 이루어지는 구조이다. 선입선출구조를 가지고 있다.
## BFS(너비 우선 탐색)
- 탐색 `시작점의 인접한 정점들을 모두 차례로 방문`한 후에,<br/>
`방문했던 정점을 시작점으로 하여` 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색한 후에 다시 너비 우선 탐색을 진행해야 하므로,<br/>
선입 선출 형태의 자료구조인 큐를 활용한다.