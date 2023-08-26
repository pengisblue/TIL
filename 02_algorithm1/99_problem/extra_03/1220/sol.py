import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [input().replace(' ', '') for _ in range(N)]
    after = list(map(lambda x: ''.join(x).replace('0', ''), list(zip(*table))))
    result = sum(list(map(lambda x: x.count('12'), after)))
    print(f'#{tc}', result)
