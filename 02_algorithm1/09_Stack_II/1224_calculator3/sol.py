import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    case = input()
    stack = []
    change = []
    priority = {'(': 0, '+': 1, '*': 2}
    # 후위 표기식 변환
    for t in case:
        if t.isdigit():
            change.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':  # 열린 괄호가 나올 때 까지 연산자를 pop() 하여 후위 표기
            while stack[-1] != '(':
                change.append(stack.pop())
            stack.pop()     # 열린 괄호 제거
        else:   # 우선 순위가 높거나 같은 연산자를 후위 표기 후 t를 스택
            while priority[t] <= priority[stack[-1]]:
                change.append(stack.pop())
            stack.append(t)
    while stack:    # 마지막 남은 연산자 정리
        change.append(stack.pop())
    # 계산
    for i in change:
        if i.isdigit():
            stack.append(int(i))
        else:   # 연산자 이면
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':    # 계산 후 다시 stack
                stack.append(num1+num2)
            else:
                stack.append(num1*num2)

    print(f'#{tc} {stack[0]}')