def enq(data):
    global rear
    global front
    if (rear+1) % cQsize == front:
        front = (front+1) % cQsize      # 앞에 있는 값에 덮어 씌우는 경우
    rear = (rear+1) % cQsize
    cQ[rear] = data


def deq():
    global front
    front = (front+1) % cQsize
    return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
print(deq())
print(deq())
print(deq())
print(deq())
