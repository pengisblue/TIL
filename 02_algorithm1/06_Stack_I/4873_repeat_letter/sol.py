import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    strings = list(input())
    stack = []      # 문자열을 하나씩 빼서 넣어줄 리스트
    i = 0
    while i < len(strings):     # 원래 문자열이 0이 될 때 까지
        if not stack:   # 비어있으면 stack
            stack.append(strings[i])
            i += 1
        else:   # 현재 문자와 스택에 있는 문자가 같으면 pop
            if strings[i] == stack[-1]:
                strings.pop(i)
                stack.pop()
            else:
                stack.append(strings[i])
                i += 1

    print(f'#{tc} {len(stack)}')