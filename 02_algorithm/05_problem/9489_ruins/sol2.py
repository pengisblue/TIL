import sys
sys.stdin = open('input1.txt')

for i in range(int(input())):
    n, k = map(int, input().split())
    p = [input().replace(' ', '') for _ in range(n)]
    # print(p)
    # print(list(zip(*p)))
    p.extend([''.join(b) for b in list(zip(*p))])
    # print(p)
    a = [b.split('0') for b in p]
    # print(a)
    print(f'#{i+1} {max([len(a[i][j]) for i in range(len(a)) for j in range(len(a[i])) if len(a[i][j])])}')
