from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 화덕 크기, 피자 개수
    cheese = list(map(int, input().split()))    # 치즈의 양
    pizza = 1   # 피자 번호
    queue = deque()
    for i in range(N):
        # 피자 번호와 함께 첫 번째 피자부터 화덕에 넣어준다
        queue.append([pizza, cheese.pop(0)])
        pizza += 1
        # print(queue)

    while queue:    # 화덕에 피자가 있는 동안
        check = queue.popleft()
        if not queue:
            # 피자를 뺏는데 더이상 화덕에 남은 피자가 없다면
            print(f'#{tc}', check[0])
        elif check[1]//2 == 0:
            if cheese:
                queue.append([pizza, cheese.pop(0)])    # 새로운 피자를 넣어준다
                pizza += 1
        elif check[1]//2 != 0:  # 피자가 녹지 않았다면
            check[1] //= 2
            queue.append(check)
        # 치즈가 다 녹았지만 마지막 피자가 아닌 것은 화덕에서 빼면 끝
