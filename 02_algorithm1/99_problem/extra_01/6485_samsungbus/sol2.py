import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선 개수
    N_list = [0] * 5001     # 노선 리스트
    for i in range(N):
        A, B = map(int, input().split())    # 노선이 다니는 정류장 범위
        N_list[A:B+1] = list(map(lambda x: x + 1, N_list[A:B+1]))   # 포함되는 노선 범위에 +1

    P = int(input())    # 정류장 갯수
    P_list = []     # 정류장 노선 개수 리스트
    for j in range(P):
        C = int(input())    # 정류장 번호
        cnt = N_list[C]     # 정류장 번호에 있는 노선 개수
        P_list.append(cnt)

    print(f'#{tc}', *P_list)
