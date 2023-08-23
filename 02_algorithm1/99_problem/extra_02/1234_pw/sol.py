import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, pw = input().split()
    N = int(N)
    pw = list(pw)
    stack = []      # 비밀번호를 스택
    for i in range(N):
        num = pw.pop()      # 비밀번호 끝자리를 pop
        if not stack:       # stack이 비어있으면 비밀번호 추가
            stack.append(num)
        else:
            if stack[-1] == num:    # 최근에 추가한 숫자와 같으면 stack에서 삭제
                stack.pop()
            else:   # 다르면 비밀번호 추가
                stack.append(num)

    stack.reverse()
    print(f'#{tc}', ''.join(map(str, stack)))
