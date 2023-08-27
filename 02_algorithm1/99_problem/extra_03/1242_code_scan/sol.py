import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.extend(input().replace('0', ' ').split())
    arr = list(set(arr))
    # print(arr)
    for i in range(len(arr)):
        pass


    # print(f'#{tc}')