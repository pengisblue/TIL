import sys
sys.stdin = open('input.txt')


def check(stack, text):
    if text == '(' or text == '{':      # 열린괄호이면 추가
        stack.append(text)
        return True
    elif text == ')':       # 닫힌 괄호일 때
        if stack and stack[-1] == '(':  # 짝이 맞으면 pop
            stack.pop()
            return True
        else:
            return False
    elif text == '}':       # 닫힌 괄호일 때
        if stack and stack[-1] == '{':  # 짝이 맞으면 pop
            stack.pop()
            return True
        else:
            return False
    else:
        return True


T = int(input())
for tc in range(1, T+1):
    texts = list(input())
    stack = []
    result = 1
    for i in range(len(texts)):
        if not check(stack, texts[i]):  # '(' -> '}' / 닫힌 괄호가 왔는데 빈 리스트
            result = 0
            break
    if stack:
        result = 0

    print(f'#{tc} {result}')
