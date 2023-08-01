def counting_sort(numbers, k):
    '''
    카운트 배열 : count_arr : k+1 번 인덱스까지
    '''
    count_arr = [0] * (k+1)
    # print(count_arr)
    # for i in range(k+1):
    #     count_arr.append(0)
    # 최종 정렬 된 값을 담을 배열
    # result의 범위 : numbers의 전체 원소 양 만큼
    result = [-1] * len(numbers)

    for i in range(len(numbers)):
        count_arr[numbers[i]] += 1
    # print(count_arr)

    # 각 요소가 들어있는 개수를 확인했으니...
    # 각 요소가 들어가야 할 인덱스를 계산하기 위해
    # 누적 값 카운팅
    for i in range(1, len(count_arr)):
        # print(count_arr[i], count_arr[i - 1])
        count_arr[i] += count_arr[i - 1]
    # print(count_arr)
    # 원본 배열의 값들을 다시 순회하면서
    # 원본 배열의 각 값들을 정렬 된 인덱스 위치에 담아주기
    for num in numbers:
        count_arr[num] -= 1
        result[count_arr[num]] = num
    print(count_arr)
    return result


numbers = [2, 3, 2, 4, 3, 3, 4, 1]
print(counting_sort(numbers, 5))