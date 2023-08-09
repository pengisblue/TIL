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

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
```