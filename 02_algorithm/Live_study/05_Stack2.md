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