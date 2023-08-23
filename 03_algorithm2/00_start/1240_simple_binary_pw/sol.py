import sys
sys.stdin = open('input.txt')

pw_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(set([input() for _ in range(N)]))
    if '1' in arr[0]:
        codes_line = arr[0]
    else:
        codes_line = arr[1]
    for i in range(M-1, 0, -1):
        if codes_line[i] == '1':
            codes = codes_line[(i+1)-56:i+1]
            break
