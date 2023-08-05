import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = input()
    count = [0]*10
    max_v = [0, 0]
    for num in numbers:
        count[int(num)] += 1
    for idx, num in enumerate(count):
        if max_v[1] <= num:
            max_v = [idx, num]

    print(f'#{tc}', *max_v)
