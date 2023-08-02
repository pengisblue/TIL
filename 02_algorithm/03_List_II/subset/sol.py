numbers = [-7, -3, -2, 5, 8]
N = 5

# numbers로 만들 수 있는 모든 경우의 수
# 1 << N == 2 ** N
# 1 왼쪽으로 3번 쉬프트 한다
# 0001 -> 1000
cnt = 0
for x in range(1<<N):   # 100000
    result = 0
    subset = []
    # 그 모든 경우의 수에서,
    # numbers의 y번째 요소가
    # x번 경우의 수에서 사용되었는지를 판별
    # x번 경우의 수가 1일때 bit -> 0001
    # numbers의 y번째 요소(0번째 요소) -> (1 << y)
    # numbers의 0번째 요소가 0001 -> (1 << 0)
    # numbers의 1번째 요소가 0010 -> (1 << 1)
    for y in range(N):
        if x & (1 << y):  # 10000, 01000, 00100, 00010, 00001
            result += numbers[y]
            subset.append(numbers[y])

    if result == 0:
        cnt += 1

print(cnt)