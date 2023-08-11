import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    stick = list(input())
    stack = []      # 괄호를 stack
    cnt = 0         # 잘린 쇠막대 개수
    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append(stick[i])      # 열린 괄호 stack
        else:   # 닫힌 괄호
            if stick[i-1] == '(':       # 레이저일 경우
                stack.pop()     # 레이저 ( 제거
                cnt += len(stack)       # 좌측 잘린 쇠막대 개수
            else:   # 쇠막대 왼쪽 끝
                stack.pop()     # 다 잘린 쇠막대 제거
                cnt += 1        # 우측 잘린 쇠막대

    print(f'#{tc} {cnt}')
