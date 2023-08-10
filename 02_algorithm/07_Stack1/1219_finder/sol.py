import sys
sys.stdin = open('input.txt')


def dfs():
    stack = [0]     # 시작은 항상 0
    visited = [False] * 100
    while stack:
        start = stack.pop()
        if visited[start] == 0:
            visited[start] = True      # 방문
            for link in range(2):
                next_n = matrix[link][start]    # 다음 방향
                if next_n == 99:    # 도착지이면
                    return 1        # 가는 길이 존재하므로 1을 반환
                if next_n != 0 and visited[next_n] == 0:    # 방문한 적이 없으면
                    stack.append(next_n)    # 스택
    else:
        return 0


for _ in range(1, 11):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    print(arr)
    matrix = [[0]*100 for _ in range(2)]    # 정점의 개수가 최대 100개이고, 선택지는 2가지를 넘지 않음
    for i in range(0, E*2, 2):
        if matrix[0][arr[i]] == 0:  # arr[i] 정점에서 다음 정점 기록이 없을 때
            matrix[0][arr[i]] = arr[i+1]    # matrix[0][arr[i]]에 다음 정점 번호를 저장
        else:
            matrix[1][arr[i]] = arr[i+1]
    print(matrix)
    print(f'#{tc}', dfs())
