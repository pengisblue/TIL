import sys
sys.stdin = open('input.txt')

def find(Page, P_find):     # 전체 페이지, 찾아야 하는 페이지
    left, right = 1, Page
    cnt = 0  # 찾는데 걸린 횟수
    while True:
        cnt += 1    # 횟수를 추가하면서 순회 시작
        mid = int((left + right) / 2)
        if mid == P_find:   # 발견
            return cnt
        elif mid < P_find:  # 찾아야 하는 페이지가 더 앞에 있을 때
            left = mid
        else:               # 찾아야 하는 페이지가 더 뒤에 있을 때
            right = mid


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result_A = find(P, A)
    result_B = find(P, B)
    if result_A == result_B:
        print(f'#{tc} 0')
    elif result_A < result_B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')
