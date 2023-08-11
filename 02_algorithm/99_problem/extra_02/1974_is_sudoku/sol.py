import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [input().replace(' ', '') for i in range(9)]      # input을 문자열 2차원 리스트 arr로 저장
    is_sudoku = list(map(lambda x: list(map(int, list(x))), arr))   # 행들을 숫자로 변환하여 저장한 리스트
    is_sudoku.extend(list(map(lambda x: list(map(int, ''.join(x))), list(zip(*arr)))))  # 열들을 숫자로 저장한 리스트 추가
    for i in range(0, 7, 3):        # 3*3 크기 사각형 안에 있는 숫자들을 순회해서
        for j in range(0, 7, 3):
            is_sudoku.append(list(map(int, list(arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]))))
            # 리스트로 묶어서 숫자로 변환시킨 후 저장
    for numbers in is_sudoku:   # 리스트를 순회하며
        numbers = set(numbers)  # 중복을 제거했을 때
        if len(numbers) < 9:    # 길이가 9 이하 == 같은 숫자가 존재
            print(f'#{tc} 0')   # 스도쿠가 아님
            break
    else:
        print(f'#{tc} 1')   # 길이가 9 == 스도쿠
