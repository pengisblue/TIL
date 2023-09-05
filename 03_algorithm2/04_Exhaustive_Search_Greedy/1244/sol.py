import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    N = len(numbers)
    numbers = set([numbers])
    change = int(change)
    changed_set = set()

    for _ in range(change):
        while numbers:
            nums = numbers.pop()
            nums = list(nums)
            for i in range(N-1):
                for j in range(i+1, N):
                    nums[i], nums[j] = nums[j], nums[i]
                    changed_set.add(''.join(nums))
                    nums[i], nums[j] = nums[j], nums[i]
        numbers, changed_set = changed_set, numbers

    result = max(numbers)
    print(f'#{tc}', result)
