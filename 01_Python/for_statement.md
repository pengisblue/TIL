# for문
```python
for 변수 in iterable (반복 가능한 객체):
    코드블록
```

## range(N) vs list
```python
lst = ['one', 'two', 'three', 'four', 'five']

# range(len(lst))의 i 번째 요소
for i in range(len(lst)):   # 0, 1, 2 ... 순서로 i 값이 나온다
    print(i, lst[i])        # iterable의 길이를 알아야함
                            # 인덱스값을 사용해서 다양한 계산 가능
    '''
    0 one
    1 two
    2 three
    3 four
    4 five
    ''' 

# 리스트의 i 번째 요소
for i in lst:   # iterable의 길이를 몰라도 된다 (range를 안써서)   
    print(i)    # 인덱스를 사용하지 않고 리스트의 요소를 불러올 수 있다
                # 인덱스값을 활용한 계산을 하기 어렵다 (인덱스를 따로 불러오는 함수가 필요함)
    '''
    one
    two
    three
    four
    five
    '''
```

## 2차원 배열에서
```python
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
```
```python
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
```
```python
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
```