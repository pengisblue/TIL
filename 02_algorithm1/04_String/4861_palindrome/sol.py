import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    strings = [input() for i in range(N)]
    strings.extend(list(map(lambda x: ''.join(x), list(zip(*strings)))))
    palindrome = ''
    for string in strings:      # 리스트의 문자열을 순회하며 palindrome 확인
        for i in range(N-M+1):        # M번째 문자까지 palindrome 확인할 때 반복 횟수
            is_palindrome = True
            for j in range(0, M//2):          # 절반을 비교해서
                if string[i+j] != string[M+i-1-j]:  # 다른 문자열이 있으면
                    is_palindrome = False       # False
                    break
            if is_palindrome:                   # string[i:M-1+i]가 palindrome 이면,
                palindrome = string[i:M+i]
                break

    print(f'#{tc} {palindrome}')
