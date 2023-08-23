import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = set(input())
    str1 = list(str1)
    dict1 = {}
    for word in str1:
        dict1[word] = 0     # {str1의 알파벳 : 0}

    str2 = input()
    max_v = 0
    for word in str2:
        if word in dict1:
            dict1[word] += 1    # 일치하는 문자가 있으면 dict에 카운트

    cnt = list(dict1.values())  # dict1의 value만 모은 list = 알파벳 개수들
    max_v = 0
    for num in cnt:
        if max_v < num:
            max_v = num

    print(f'#{tc} {max_v}')
