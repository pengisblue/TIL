import sys
sys.stdin = open('input.txt')


def cal(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 // n2


def forth(calculate):
    stack = []
    for i in calculate:
        if i == '.':    # 계산 종료
            # 스택에 결과값 하나만 남아있는게 아니면
            if len(stack) != 1:
                return 'error'
            else:   # 결과값 리턴
                return stack[0]
        elif i.isdigit():   # 숫자이면
            stack.append(int(i))    # 스택
        else:   # 숫자가 아니면 == 연산자 이면
            # 스택에 계산할 숫자가 2개 이상이어야 함
            if len(stack) > 1:
                num2 = stack.pop()  # 계산 순서 주의
                num1 = stack.pop()
                # 연산자 i 에 따라 계산하여 다시 스택
                stack.append(cal(i, num1, num2))
            else:
                return 'error'


T = int(input())
for tc in range(1, T+1):
    need_cal = input().split()
    print(f'#{tc}', forth(need_cal))
