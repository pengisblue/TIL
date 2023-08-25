import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 인덱스의 편의를 위해 201개로 만들어줌
    corridor = [0] * 201
    for _ in range(N):
        now, back = map(int, input().split())
        # 짝수, 홀수로 나눈 방 번호
        now = now // 2 + now % 2
        back = back // 2 + back % 2
        # 방을 옮기면서 지나간 길을 표시해줌
        if now > back:
            corridor[back:now+1] = list(map(lambda x: x + 1, corridor[back:now+1]))
        else:
            corridor[now:back+1] = list(map(lambda x: x + 1, corridor[now:back+1]))

    print(f'#{tc}', max(corridor))
