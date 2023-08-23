import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()
    palindrome = 1
    for i in range(len(N)//2):
        if N[i] != N[-1-i]:
            palindrome = 0

    print(f'#{tc} {palindrome}')
