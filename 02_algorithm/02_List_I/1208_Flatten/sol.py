import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    move = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 박스별 높이를 담은 리스트
    cnt_arr = [0] * 101  # 0 ~ 100까지 카운트 (최대 상자 높이)
    box_arr = [0] * 100  # 가로의 길이(len(boxes))는 항상 100

    for i in range(100):
        cnt_arr[boxes[i]] += 1

    for i in range(1, 101):
        cnt_arr[i] += cnt_arr[i - 1]

    for box in boxes:
        cnt_arr[box] -= 1
        box_arr[cnt_arr[box]] = box

    # cnt_arr[i] == box_arr 에서 i가 시작되는 index 값

    max_box, min_box = box_arr[-1], box_arr[0]  # 가장 높은, 낮은 box
    for i in range(1, move+1):
        # print(i,'번', max_box, min_box, "이동 전")
        box_arr[cnt_arr[max_box]] -= 1  # 가장 높은 박스 중 맨 앞에 있는 값 -1
        box_arr[cnt_arr[min_box+1]-1] += 1  # 가장 낮은 박스 중 맨 뒤에 있는 값 +1
        cnt_arr[max_box] += 1  # 가장 높은 박스의 시작 index +1
        cnt_arr[min_box+1] -= 1  # 두 번째 박스의 시작 index -1
        max_box, min_box = box_arr[-1], box_arr[0]
        # print(max_box, min_box, "이동 후")
        # print('----------')
        if max_box - min_box <= 1:
            break

    print(f'#{tc} {max_box - min_box}')
