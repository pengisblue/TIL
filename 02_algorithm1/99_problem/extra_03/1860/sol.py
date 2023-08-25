import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # 손님 수, 붕어빵 만드는 시간, 붕어빵 개수
    arrive = list(map(int, input().split()))
    time = 0
    fish = 0
    if 0 in arrive:
        print(f'#{tc}', 'Impossible')
        continue
    while time < max(arrive):
        time += 1
        if time % M == 0:
            fish += K
        if time in arrive:
            cnt = arrive.count(time)
            fish -= cnt
        if fish < 0:
            print(f'#{tc}', 'Impossible')
            break
    else:
        print(f'#{tc}', 'Possible')
