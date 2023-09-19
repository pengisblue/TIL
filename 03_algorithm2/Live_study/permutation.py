# 순열
# nPr: n개의 요소 중 r개를 사용하는 경우의 수
def perm(now, r):
    if now == r:
        print(check)
        return
    else:
        # 완전 검색
        for i in range(N):
            if visited[i]: continue
            visited[i] = True   # i번쨰 요소를 쓴다?
            # 실제 사용 여부는 check에 표기
            check[now] = arr[i]
            perm(now + 1, r)
            visited[i] = False

# 반복에 대한 이해
# 완전 검색 : Brute Force
# 재귀 함수에 대한 이해
arr = [1, 2, 3]
N = len(arr)
# 각 요소의 사용여부
visited = [0, 0, 0]
# visited = [0] * (N + 1)
# 실제 순열에 구성되는 요소들을 담을 리스트
check = [0] * N

perm(0, N)