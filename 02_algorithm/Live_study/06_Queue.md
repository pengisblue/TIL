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

### 우선순위 큐
- 우선순위를 가진 항목들을 저장하는 큐
- 배열을 사용하므로 삽입이나 삭제 연산이 일어날 때 원소 재배치에 소요되는 시간이나 메모리 낭비가 큼