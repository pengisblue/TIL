import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers, count = input().split()
    # print(numbers, count)
    count = int(count)

    # print(set(numbers))
    # print(set([numbers]))
    nums = set([numbers])
    SET = set()

    for _ in range(count):
        while nums:
            n = nums.pop()
            n = list(n)
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    # print(i, j)
                    # print(n[i], n[j])
                    n[i], n[j] = n[j], n[i]
                    SET.add(''.join(n))
                    print(SET)
                    n[i], n[j] = n[j], n[i]
        nums, SET = SET, nums

    result = max(nums)
    print(f'#{tc} {result}')
