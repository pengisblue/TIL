import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    result = ''
    for num in prime:
        cnt = 0
        while N % num == 0:  # number % num == 0:     # 나머지가 0인 동안 반복
            N /= num
            cnt += 1
        result += str(cnt)

    print(f'#{tc} {" ".join(result)}')
