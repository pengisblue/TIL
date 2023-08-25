# 성은햄 풀이
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    print(f'#{tc + 1} ', end='')
    input_str = [input() for _ in range(5)]
    for i in range(15):
        for j in range(5):
            if len(input_str[j]) > i:
                print(input_str[j][i], end='')

    print()