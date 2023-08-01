import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    move = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 박스 높이
    for cnt in range(move):
        