# now
# r
# idx : 이번 회차 조사 시작 지점
def comb(now, r, idx):
    if now == r:
        print(check[:r])
    else:
        for i in range(idx, len(num)):
            check[now] = num[i]
            comb(now + 1, r, i + 1)

num = [1, 2, 3]
# 실제 조합에 구성되는 요소들을 담을 리스트
check = [0] * len(num)
comb(0, 2, 0)
