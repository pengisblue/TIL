import sys
sys.stdin = open('input.txt')


def search(row, acc):
    global result
    # 가지치기
    # 내 누적잢이 최종 결과값보다 한 번이라도 커지면, 더 이상 조사 X
    if acc > result:
        return
    # 언제까지 조사 : now가 N이 되면 모든 열에 대한 탐색
    if row == N:
        if acc < result:
            result = acc
    else:
        # 현재 행(now)에서 가능한 모든 열(col)를 탐색
        for col in range(N):
            # 아직 방문한 적 없다면,
            if visited[col] == 0:
                visited[col] = 1
                search(row + 1, acc + arr[row][col])
                visited[col] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N     # 최솟값 초기화
    visited = [0] * N
    # 시작값, 누적값
    search(0, 0)
    print(f'#{tc} {result}')
