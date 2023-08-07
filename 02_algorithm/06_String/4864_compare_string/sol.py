import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        check = str2[i:len(str1)+i]
        if str1 == check:
            result = 1
            break

    print(f'#{tc} {result}')
