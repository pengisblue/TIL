import sys
sys.stdin = open('input.txt')
print(int('0001101', 2))
print(int('0011001', 2))
print(int('0010011', 2))
print(int('0111101', 2))
print(int('0100011', 2))
print(int('0110001', 2))
print(int('0101111', 2))
print(int('0111011', 2))
print(int('0110111', 2))
print(int('0001011', 2))


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