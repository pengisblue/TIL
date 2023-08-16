import sys
sys.stdin = open('input.txt')


# 가위바위보 승자 구하기  승자의 인덱스를 리턴
def win(idx1, idx2):
    if card_nums[idx1] == '1':
        if card_nums[idx2] == '1':
            return idx1
        elif card_nums[idx2] == '2':
            return idx2
        else:
            return idx1
    elif card_nums[idx1] == '2':
        if card_nums[idx2] == '1':
            return idx1
        elif card_nums[idx2] == '2':
            return idx1
        else:
            return idx2
    else:
        if card_nums[idx2] == '1':
            return idx2
        elif card_nums[idx2] == '2':
            return idx1
        else:
            return idx1


# 가위바위보 할 사람 구하기
def game(front, back):  # 리스트의 인덱스를 인자로 받는다
    if back - front == 0:   # front == back
        return front
    elif back - front == 1:     # 옆사람
        return win(front, back)     # 가위바위보
    else:
        mid = (front + back) // 2   # 가운데를 찾아서
        a = game(front, mid)    # 앞과
        b = game(mid+1, back)   # 뒤로 나눈다
        return win(a, b)    # 가위바위보


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_nums = list(input().split())
    print(f'#{tc}', game(0, N-1) + 1)   # 인덱스를 리턴 받았으므로 + 1
