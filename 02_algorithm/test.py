# arr: 원본 배열
# N: 배열의 길이
# key: 타겟
def binary_search(arr, N, key):
    start = 0
    end = N-1  # 끝 인덱스
    while start <= end:  # 시작지점이 끝지점보다 작거나 같은 동안
        mid = (start + end) // 2 # 중앙 인덱스
        # 중앙 위치가 내가 찾는 대상이라면
        if arr[mid] == key:
            return True
        # 아닌데, 중앙 위치 값이 내 키 값보다 크면
        elif arr[mid] > key:
            end = mid -1
        # 아닌데, 중앙 위치 값이 내 키 값보다 작으면
        else:
            start = mid + 1
    return False

numbers = list(range(1, 30, 2))
print(numbers)
N = len(numbers)
target = 25
# 이진 탐색