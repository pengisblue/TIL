import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = [arr.pop(arr.index(max(arr))) if i % 2 == 0 else arr.pop(arr.index(min(arr))) for i in range(10)]
    print(f'#{tc}', *ans)
