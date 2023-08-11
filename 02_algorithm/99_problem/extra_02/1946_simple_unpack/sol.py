import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    txt = ''
    for i in range(N):
        C, K = input().split()
        txt += C * int(K)   # 하나의 문자열로 저장
    print(f'#{tc}')
    i = 0   # txt index
    while len(txt) - i > 10:
        print(txt[i:i+10])  # 10글자씩 출력
        i += 10
    print(txt[i:])      # 나머지 글자 출력
