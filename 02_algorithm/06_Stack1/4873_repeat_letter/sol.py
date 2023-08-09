import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    strings = list(input())
    stack = []
    i = 0
    while i < len(strings):
        if not stack:
            stack.append(strings[i])
            i += 1
        else:
            if strings[i] == stack[-1]:
                strings.pop(i)
                stack.pop()
            else:
                stack.append(strings[i])
                i += 1

    print(f'#{tc} {len(stack)}')