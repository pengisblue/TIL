arr = [
    ['one', 'two', 'three', 'four'], 
    ['1st', '2nd', '3rd', '4th'], 
    [1, 2, 3, 4], 
    ]

for i in range(len(arr)):
    print(i, arr[i])
    '''
    0 ['one', 'two', 'three', 'four']
    1 ['1st', '2nd', '3rd', '4th']
    2 [1, 2, 3, 4]
    '''

for i in arr:
    print(i)
    '''
    ['one', 'two', 'three', 'four']
    ['1st', '2nd', '3rd', '4th']
    [1, 2, 3, 4]
    '''

# 예쁘게 보기
for i in range(3):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()
    '''
    one two three four
    1st 2nd 3rd 4th
    1 2 3 4
    '''

# 2중 for문 행(→) 순서대로 출력
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(i, j, ',', arr[i][j])
    print('----')
    '''
    0 0 , one
    0 1 , two
    0 2 , three
    0 3 , four
    ----
    1 0 , 1st
    1 1 , 2nd
    1 2 , 3rd
    1 3 , 4th
    ----
    2 0 , 1
    2 1 , 2
    2 2 , 3
    2 3 , 4
    ----
    '''

# 2중 for문 열(↓) 순서대로 출력
for j in range(len(arr[i])):
    for i in range(len(arr)):
        print(i, j, ',', arr[i][j])
    print('----')
    ''''
    0 0 , one
    1 0 , 1st
    2 0 , 1
    ----
    0 1 , two
    1 1 , 2nd
    2 1 , 2
    ----
    0 2 , three
    1 2 , 3rd
    2 2 , 3
    ----
    0 3 , four
    1 3 , 4th
    2 3 , 4
    ----
    '''

# range를 사용 안했을 때
for i in arr:       # 배열 안의 리스트를 순서대로 반환 [[여, 기], [있, 는], [값, 들]]
    for j in i:     # 그 리스트 안의 요소를 순서대로 반환 [여, 기]
        print(j)
    '''
    one
    two
    three
    four
    1st
    2nd
    3rd
    4th
    1
    2
    3
    4
    '''
# 연산

for i in range(len(arr)):
    for j in range(len(arr)):   # 첫 번째 반복 값
        print(i)                # 0
        print(i + 1)            # 1
        print(j)                # 0
        print(j + 1)            # 1

for i in arr:
    for j in i:         # 첫 번째 반복 값
        print(i)        # ['one', 'two', 'three', 'four']
        print(i + 1)    # TypeError: can only concatenate list (not "int") to list
        print(j)        # one
        print(j + 1)    # TypeError: can only concatenate str (not "int") to str