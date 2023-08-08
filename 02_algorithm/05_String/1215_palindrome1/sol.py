import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())    # 회문의 길이
    words = [list(input()) for i in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            palindrome = True
            for k in range(N//2):
                if words[i][j+k] != words[i][j+N-1-k]:
                    palindrome = False
                    break
            if palindrome:
                cnt += 1
            palindrome = True
            for k in range(N//2):
                if words[j+k][i] != words[j+N-1-k][i]:
                    palindrome = False
                    break
            if palindrome:
                cnt += 1

    print(f'#{tc} {cnt}')