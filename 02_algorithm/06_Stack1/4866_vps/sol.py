import sys
sys.stdin = open('input.txt')

def check(stack, text):
    if text == '(' or text == '{':
        stack.append(text)
        return True
    elif text == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            return True
        else:
            return False
    elif text == '}':
        if stack and stack[-1] == '{':
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
        if not check(stack, texts[i]):
            result = 0
            break
    if stack:
        result = 0

    print(f'#{tc} {result}')
