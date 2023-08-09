import sys
sys.stdin = open('input.txt')


def pascal(n):
    global memo
    if n >= 2 and memo[n-1] == ([0] * n):
        for i in range(n):
            if i == 0 or i == n-1:
                memo[n-1][i] = 1    # 1번째와 n번째 숫자는 1
            else:   # N번째 줄 i번째 숫자는 N-1번째 줄 i-1, i번째 숫자 합
                memo[n-1][i] = pascal(n-1)[i-1] + pascal(n-1)[i]
    return memo[n-1]    # 파스칼 삼각형의 N번째 줄 리스트를 return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    # pascal()의 1 ~ N번째 리스트를 담아둘 리스트 memo
    memo = [[0]*i for i in range(1, N+1)]
    memo[0] = [1]   # 1번째
    for i in range(1, N+1):
        print(*pascal(i))
