T = int(input())
for i in range(1, T + 1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = max(N, M) - min(N, M) + 1
    ans = []
    for j in range(cnt):
        cal = 0
        if M >= N:
            for k in range(N):
                cal += A[k] * B[j + k]
            ans.append(cal)
        else:
            for k in range(M):
                cal += A[j + k] * B[k]
            ans.append(cal)
    print(f'#{i} {max(ans)}')