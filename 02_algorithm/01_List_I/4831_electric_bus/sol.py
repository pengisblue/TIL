import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # 최대 이동 정류장, 종점, 충전기 갯수
    stop_numbers = list(map(int, input().split()))
    line = [0] * (N + 1)
    bus_idx = 0  # 버스 위치
    cnt_c = 0  # 충전 횟수

    for num in stop_numbers:  # 충전기가 위치한 곳 i == line[i]
        line[num] += 1

    while bus_idx + K < N:
        for i in range(bus_idx + K, bus_idx, -1):  # 가장 멀리갈 수 있는 거리부터 역으로 순회
            if line[i]:  # 충전기가 있으면
                bus_idx = i  # 버스를 이동
                cnt_c += 1  # 충전 횟수 증가
                print(bus_idx, cnt_c)
                break
            elif i == bus_idx + 1:  # for 문을 끝까지 순회하면
                cnt_c = 0
        if cnt_c == 0:
            break

    print(f'#{tc} {cnt_c}')
