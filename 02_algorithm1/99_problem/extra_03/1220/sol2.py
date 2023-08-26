import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 테이블을 아래 방향으로 순회
    for j in range(N):
        magnet = 0
        for i in range(N):
            if table[i][j]:     # 테이블에 자석이 있을 때
                # 이전 자석이 내려가는 자석인데 현재 자석이 올라가는 자석이면
                if magnet == 1 and table[i][j] == 2:
                    result += 1
                magnet = table[i][j]

    print(f'#{tc}', result)
