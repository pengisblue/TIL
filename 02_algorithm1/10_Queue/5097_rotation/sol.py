from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque()
    # 숫자들을 리스트로 받아서 큐에 넣어줌
    queue.extend(list(map(int, input().split())))
    for _ in range(M):      # 맨 앞 숫자를 빼서 맨뒤에 넣는 작업
        front = queue.popleft()
        queue.append(front)

    print(f'#{tc}', queue.popleft())