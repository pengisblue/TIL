import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    numbers = list(numbers)
    change = int(change)
    N = len(numbers)
    max_result = sorted(numbers, reverse=True)
    print(''.join(numbers))
    print(''.join(max_result))
    print(f'#{tc}', change)