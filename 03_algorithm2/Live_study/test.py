def perm(idx, chosen):
    if idx == N:
        tmp = []
        for i in chosen:
            tmp.append(data[i])
        result.append(tmp)
        return

    # 모든 N개의 원소를 조사했는지 판단
    for i in range(N):
        # i번째에 쓰겠다고 이전에 판정된 적이 있다면,
        # 현재 조사 대상을 i번째에 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[idx] = i     # idx번째 대상을 i번째에 둬서 사용
        perm(idx+1, chosen)
        # chosen[idx] = -1


N = 4
data = '1247'
result = []
# i번째에 들어갈 수 있는 0, N-1 까지를 제외한
chosen = [-1] * N
perm(0, chosen)
print(result)