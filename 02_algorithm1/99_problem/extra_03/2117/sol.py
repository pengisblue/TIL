import sys
sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]      # 반시계
dj = [0, -1, 0, 1]
mv_i = [1, 1, -1, -1]   # 대각선 이동
mv_j = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 도시 크기, 가구 당 지불 가능 비용
    city = [list(map(int, input().split())) for _ in range(N)]
    total_house = 0      # 전체 가구의 수
    for i in range(N):
        total_house += sum(city[i])
    K = 1   # 영역 크기
    # 모든 가구가 서비스 받을 때 지불 가능한 금액보다 방범 비용이 커지기 전까지
    while K**2 + (K-1)**2 <= total_house * M:
        K += 1
    max_K = K - 1   # 최대 영역의 크기
    max_house = 0   # 서비스 가능한 최대 가구 수
    for i in range(N):
        for j in range(N):
            house = city[i][j]      # 중심으로 부터 방범 영역까지의 가구 수
            for k in range(1, max_K+1):     # 최대 운영 가능 영역까지 영역의 크기를 순회
                cost = k**2 + (k-1)**2      # 영역이 k 일 때, 방범에 필요한 비용
                if cost % M:
                    min_house = cost // M + 1   # 영역이 k 일 때, 서비스에 필요한 최소 가구 수
                else:
                    min_house = cost // M
                dis = k - 1                 # 영역이 k 일 때, 탐색 거리
                for way in range(4):    # 반시계 방향으로 순회하면서
                    for go in range(dis):   # 대각선 둘레 탐색
                        dx = i + (di[way]*dis) + (mv_i[way]*go)
                        dy = j + (dj[way]*dis) + (mv_j[way]*go)
                        if 0 <= dx < N and 0 <= dy < N:     # 탐색 방향이 인덱스 범위 안에 있을 때,
                            if city[dx][dy] == 1:   # 집이 있으면
                                house += 1      # 카운트
                # 영역 내 가구 수가 최소 가구 수 보다 많을 때, 최대 서비스 가구 수 보다 크면
                if house >= min_house and house > max_house:
                    max_house = house       # 최대 서비스 가구 수 변경

    print(f'#{tc}', max_house)
