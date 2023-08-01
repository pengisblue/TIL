import sys
# open 함수의 인자는
# 내가 열고자 하는 파일의 경로와 이름
sys.stdin = open('input.txt')

# input 함수의 반환값은 항상 문자열
# map 함수를 써서 넘겨받은 문자열을
# 공백 기준으로 쪼갠 다음,
# 각각을 정수로 바꿔서
# 리스트에 담는다
data = list(map(int, input().split()))
print(data)
