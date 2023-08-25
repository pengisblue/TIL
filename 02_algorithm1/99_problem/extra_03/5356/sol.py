import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for word in arr:
        if max_len < len(word):
            max_len = len(word)
    for word in arr:
        word.extend(['@']*(max_len - len(word)))
    print(f'#{tc}', ''.join(list(map(lambda x: ''.join(x).replace('@', ''), list(zip(*arr))))))