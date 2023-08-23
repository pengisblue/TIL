import sys
sys.stdin = open('input.txt')

A = list(range(1, 13))
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 부분집합 원소의 수, 부분 집합의 합
    subset_k = []
    for i in range(1 << 12):  # 모든 부분 집합
        tmp = []
        sum_sub = 0  # 부분 집합의 합
        for j in range(12):
            if i & (1 << j):
                tmp.append(A[j])  # 임시로 리스트에 저장
                sum_sub += A[j]   # 부분 집합의 합을 계산
        if sum_sub == K:          # 합이 일치할 때
            subset_k.append(tmp)  # subset_k 리스트에 저장

    idx, cnt = 0, len(subset_k)
    while cnt > 0:
        if len(subset_k[idx]) != N:  # subset_k[idx]의 원소 개수가 N과 다르면
            subset_k.remove(subset_k[idx])  # 삭제
        else:                       # 같으면
            idx += 1                # 다음 idx로
        cnt -= 1

    ans = len(subset_k)
    print(f'#{tc} {ans}')
