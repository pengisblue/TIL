import sys
sys.stdin = open('input.txt')


def make_candidates(visited, now, c):
    in_perm = [False] * NMAX
    for i in range(1, now):
        in_perm[visited[i]] = True
    ncans = 0
    for i in range(1, N+1):
        if in_perm[i] == False:
            c[ncans] = i
            ncans += 1
    return ncans


def backtrack(visited, now, end, acc):
    global result
    # 가지치기
    if acc > result:
        return

    c = [0] * MAXCANDIDATES

    # 아직 누적값이 result보다 크지 않아서, 최솟값이 될 가능성이 남아 있다면,
    # 언제까지 조사할 것인가
    if now == end:  # 모든 열에 대해 조사
        # 그래서 지금까지 쌓이 acc가 result보다 작아서
        # 최솟값을 갱신 할 수 있는지 확인
        if acc < result:
            result = acc
    else:
        now += 1
        # 현재 위치의 후보 생성
        ncands = make_candidates(visited, now, c)   # 후보군 생성하고, 그 후보군의 길이를 반환
        for i in range(ncands):
            visited[now] = c[i]
            backtrack(visited, now, end, acc + arr[now-1][visited[now]-1])
            visited[now] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    '''
    [
        [2, 1, 2],
        [5, 8, 5],
        [7, 2, 2]
    ]
    '''

    result = 10 * N     # 최솟값 초기화
    # result = sum(sum(arr, []))  # 모든 배열의 합을 최솟값으로 정할 수도 있음
    # 2차원 리스트 돌리는거라 시간이 많이 걸림
    MAXCANDIDATES = N   # 최대 후보군 수
    NMAX = N + 1
    visited = [False] * NMAX
    # 방문 표시, 시작점, 끝점, 누적값
    backtrack(visited, 0, N, 0)

    print(f'#{tc} {result}')
