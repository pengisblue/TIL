import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # 최대 이동 정류장, 종점, 충전기 갯수
    stop_numbers = list(map(int, input().split()))
    line = [0] * (N + 1)
    bus_idx = 0
    for num in stop_numbers:
        line[num] += 1

    while bus_idx < N:
        for i in range(K, bus_idx, -1):
            if
