import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 정수의 개수, 구간의 개수
    arr = list(map(int, input().split()))
    for index in range(N-M+1):  # arr 순회(구간 끝이 닿는 마지막 범위 까지)
        interval = 0  # 구간의 합 초기화
        for i in range(M):  # 구간 순회
            interval += arr[index + i]  # 구간 합 더해줌

        if index == 0:  # 최소, 최대 지정
            min_sum, max_sum = interval, interval
        else:  # 최소, 최대 비교
            if min_sum > interval:
                min_sum = interval
            if max_sum < interval:
                max_sum = interval
    result = max_sum - min_sum
    print(f'#{tc} {result}')

