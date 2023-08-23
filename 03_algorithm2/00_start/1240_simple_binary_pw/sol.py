import sys
sys.stdin = open('input.txt')

pw_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(set([input() for _ in range(N)]))    # 중복되는 줄을 제거하고 input 받기
    # arr: 0만 있는 배열 or pw가 있는 배열
    if '1' in arr[0]:   # 1이 있으면 pw
        codes_line = arr[0]
    else:
        codes_line = arr[1]
    # 코드의 끝은 무조건 1이므로 뒤에서 부터 탐색해서 1이 시작되는 부분부터 56자리 추출
    for i in range(M-1, 0, -1):
        if codes_line[i] == '1':
            codes = codes_line[(i+1)-56:i+1]
            break
    hack = 0    # 올바른 암호코드인지 확인할 변수
    pw = 0      # 암호코드
    for i in range(0, 50, 7):
        if i % 2 == 0:      # 홀수번째는 0, 14, 28, 42 인덱스
            hack += pw_code[codes[i:i+7]] * 3
        else:               # 짝수번째는 7, 21, 35, 49
            hack += pw_code[codes[i:i+7]]
        pw += pw_code[codes[i:i+7]]

    if hack % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {pw}')
