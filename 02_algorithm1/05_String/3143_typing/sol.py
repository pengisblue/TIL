import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N, M = len(A), len(B)
    i = 0       # index
    cnt = 0     # A.count(B)
    while i <= N-M:
        if A[i:M+i] == B:   # B가 있으면
            cnt += 1
            i += M          # 탐색 인덱스를 B 길이만큼 넘어가기
        else:
            i += 1

    result = N - ((M-1) * cnt)
    print(f'#{tc} {result}')
