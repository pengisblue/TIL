import sys

sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())  # 건물의 개수
    buildings = list(map(int, input().split()))  # 건물의 높이
    result = 0  # 조망권이 확보된 세대 수
    for index in range(2, N - 2):  # 앞, 뒤 0 0을 제외하고 반복
        building = buildings[index]
        front1 = building - buildings[index - 1]
        front2 = building - buildings[index - 2]
        back1 = building - buildings[index + 1]
        back2 = building - buildings[index + 2]
        # view = min(front1, front2, back1, back2)  # buildings[index]의 조망권이 확보된 세대 수
        views = [front1, front2, back1, back2]
        real_view = front1
        for view in views:
            if real_view > view:
                real_view = view
        if real_view < 0:
            real_view = 0
        result += real_view
    print(f'#{test} {result}')
