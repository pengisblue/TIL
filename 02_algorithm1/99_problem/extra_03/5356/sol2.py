import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    st = [input() for i in range(5)]
    cnt = max([len(st[i]) for i in range(5)])
    print(f'#{tc}', end=' ')
    for i in range(cnt):
        for j in range(5):
            try:
                print(st[j][i], end='')
            except IndexError:
                pass
    print()
