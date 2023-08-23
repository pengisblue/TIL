import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    stack = [prices.pop()]
    margin = 0
    for _ in range(N-1):
        if stack[-1] > prices[-1]:  # 스택이 가격보다 클 때: margin = stack - price
            margin += stack[-1] - prices[-1]
            prices.pop()
        else:   # 스택이 가격보다 작거나 같을 때: 가격을 스택에 추가 -> 판매가 변경
            stack.append(prices.pop())

    print(f'#{tc}', margin)
