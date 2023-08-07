import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for i in range(N)]
    flowers = 0     # max 꽃가루
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            tmp = 0     # 꽃가루 개수를 세어줄 임시 변수
            tmp += balloons[i][j]
            long = tmp
            for k in range(4):
                for l in range(1, long+1):
                    if 0 <= i + (l*di[k]) < N and 0 <= j + (l*dj[k]) < M:
                        tmp += balloons[i + (l*di[k])][j + (l*dj[k])]
            if flowers < tmp:
                flowers = tmp

    print(f'#{tc} {flowers}')
