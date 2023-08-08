import sys
sys.stdin = open('input.txt')

# 딕셔너리에 각 문자열의 숫자 값을 저장
num_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for tc in range(1, T+1):
    test, N = input().split()
    N = int(N)
    numbers = input().split()   # 문자열 숫자 리스트
    cnt_arr = [0] * 10      # 카운팅 정렬 사용
    result = [0] * (N+1)
    for num in numbers:
        cnt_arr[num_dic[num]] += 1      # 각 숫자의 개수 카운트
    for i in range(1, 10):
        cnt_arr[i] += cnt_arr[i - 1]    # 누적 인덱스
    for num in numbers:
        result[cnt_arr[num_dic[num]]] = num     # cnt_arr에서 인덱스 번호를 얻어서 result에 num을 할당
        cnt_arr[num_dic[num]] -= 1

    result.remove(0)
    print(test)
    print(*result)
