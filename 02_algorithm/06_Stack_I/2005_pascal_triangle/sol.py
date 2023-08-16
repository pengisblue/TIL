import sys
sys.stdin = open('input.txt')


def pascal(n):
    global memo
    if n >= 3 and memo[n-1] == ([1] * n):   # 3번째 줄 부터 리스트가 1로 채워져 있을 때 (값을 구하지 않았을 때)
        for i in range(1, n-1):     # N번째 줄 i번째 숫자는 N-1번째 줄 i-1, i번째 숫자 합
            memo[n-1][i] = pascal(n-1)[i-1] + pascal(n-1)[i]
    return memo[n-1]    # 파스칼 삼각형의 N번째 줄 리스트를 return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    # pascal()의 1 ~ N번째 리스트를 담아둘 리스트 memo
    memo = [[1]*i for i in range(1, N+1)]   # N번째 줄까지 1로 초기화
    for i in range(1, N+1):
        print(*pascal(i))
