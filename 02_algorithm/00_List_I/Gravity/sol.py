import sys

sys.stdin = open('input.txt')

T = int(input())  # 전체 테스트 케이스 수

# T번 만큼 순회하면서 각 tc에 대한 문제 해결
for tc in range(1, T+1):
    N = int(input())  # 상자들이 담겨있는 칸의 개수
    boxes = list(map(int, input().split()))  # 각 상자들의 높이가 담겨 있는 값
    result = 0  # 최종 결괏값
    for i in range(N):
        # i 번째 상자가 떨어질 수 있는 최대
        max_H = N - (i+1)  # 전체 길이 - (내 위치(index) + 1)
        # 내 다음에 오는 상자들 중에 나보다 크거나 같은 값들 찾기
        for j in range(i+1, N):  # 내 다음부터 끝까지
            # 내 높이보다, j번째 위치가 크거나 같은 값
            if boxes[i] <= boxes[j]:
                max_H -= 1
        # i번째 최대로 떨어질 수 있는 낙차 값이
        # 현재 내가 기록해둔 최종 결괏값보다 크다면
        if result < max_H:
            result = max_H
    print(f'#{tc} {result}')
