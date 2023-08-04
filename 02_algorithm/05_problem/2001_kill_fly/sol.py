import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flys = [list(map(int, input().split())) for i in range(N)]
    kill = 0    # 가장 많이 죽은 파리 수
    for i in range(N):
        for j in range(N):
            tmp = 0     # 죽은 파리 임시변수
            for k in range(M):
                for l in range(M):
                    if 0 <= i+k < N and 0 <= j+l < N:
                        tmp += flys[i+k][j+l]
            if kill < tmp:
                kill = tmp

    print(f'#{tc} {kill}')