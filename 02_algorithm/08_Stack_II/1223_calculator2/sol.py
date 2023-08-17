import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    case = input()
    stack = []
    change = []     # 후위 표기식으로 정렬할 리스트
    priority = {'+': 1, '*': 2}
    # 후위 표기식 변환
    for t in case:
        if t.isdigit():
            change.append(t)
        else:
            # 스택에 있는 연산자의 우선순위가 더 높거나 같으면 기존 연산자를 pop() 후에 연산자를 스택
            while stack and priority[t] <= priority[stack[-1]]:
                change.append(stack.pop())
            stack.append(t)
    while stack:    # 스택에 남은 연산자 pop()
        change.append(stack.pop())
    # 계산
    for i in change:
        if i.isdigit():
            stack.append(int(i))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)
    print(f'#{tc}', stack[0])
