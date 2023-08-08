import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split('0'))
    result = 0
    for i in range(len(arr)):
        if result < len(arr[i]):
            result = len(arr[i])

    print(f'#{tc} {result}')
