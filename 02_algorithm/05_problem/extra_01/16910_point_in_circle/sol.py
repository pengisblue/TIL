import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N은 반지름
    dx = [-1, 1]    # 좌, 우
    x, y = 0, 0     # 중심점
    points = 0      # 점 개수
    for i in range(x-N, x+N+1):   # 원의 아래부터 위로 올라가면서
        for j in range(y+N+1):  # 원의 오른쪽 탐색
            if (x-i)**2 + (y-j)**2 <= N**2:
                points += 1

    result = (2 * points) - (2 * N + 1)     # 원의 반대편 추가 - 겹치는 y축
    print(f'#{tc} {result}')
