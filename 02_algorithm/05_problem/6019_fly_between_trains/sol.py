import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())  # 기차 사이 거리, A 속력, B 속력, 파리 속력
    time = D / (A + B)  # 두 기차가 충돌하기까지 걸린 시간
    result = F * time

    print(f'#{tc} {result}')
