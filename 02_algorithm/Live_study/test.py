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
