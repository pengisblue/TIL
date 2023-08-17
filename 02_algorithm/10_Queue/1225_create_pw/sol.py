import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    numbers = list(map(int, input().split()))
    minus = 0   # 감소시킬 수 
    while True:
        minus = minus % 5 + 1   # 1, 2, 3, 4, 5 반복
        num = numbers.pop(0) - minus    # 맨 앞 숫자를 pop()해서 감소 시킨 뒤
        if num < 0:     # 0보다 작아지면 0으로 바꿔주고
            num = 0
        numbers.append(num)     # 맨 뒤에 다시 추가
        if num == 0:    # 반복 종료 조건
            break
            
    print(f'#{tc}', *numbers)
