# 7/20 강의
## 제어문
> <u>조건</u>에 따라 코드 블록을 실행하거나 <u>반복적</u>으로 코드를 실행

## 조건문
> if / elif / else
### 'if' statement
```python
if 표현식:
    코드 블록
elif 표현식:
    코드 블록
else:
    코드 블록
```
- **조건을 순차적으로 비교 (동시에 검사하는 것이 아님)**

## 반복문
### 'for' statement
> 임의의 iterable한 객체를 순서대로 반복
```python
for 변수 in 반복 가능한 객체:
    코드 블록
```
- 문자열 순회
- range 순회
- 인덱스로 리스트 순회
- 중첩 리스트 순회
    ```python
    elements = [['A', 'B'],['c', 'd']]

    for elem in elements:
        for item in elem:
            print(item)

    '''
    A
    B
    c
    d
    '''
    ```
    ```python
    
    ```
### 'while' statement
> 주어진 조건이 True인 동안 코드를 반복  
> == 조건 식이 False가 될 때 까지 반복
```python
while 조건식:
    코드 블록
```
- 사용자 입력에 따른 반복
    ```python
    number = int(input('양의 정수를 입력해 주세요.: '))

    while number <= 0:
        if number < 0:
            print('음수를 입력했습니다.')
        else:
            print('0은 양의 정수가 아닙니다.')

        number = int(input('양의 정수를 입력해주세요.: '))

    print('잘했습니다!')

    '''
    양의 정수를 입력해 주세요.: 0
    0은 양의 정수가 아닙니다.  
    양의 정수를 입력해주세요.: -1
    음수를 입력했습니다.       
    양의 정수를 입력해주세요.: 1
    잘했습니다!
    '''
    ```

### for or while ?
- for
    - 반복 횟수가 명확하게 정해져 있는 경우
    - list, tuple, str 등과 같은 시퀀스 형식의 데이터를 처리할 때
<br><br>
- while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 사용자의 입력을 받아서 특정 조건이 충족될 때 까지 반복하는 경우

### 반복 제어
- break
> 반복을 즉시 중지
```python
# 첫 번째 짝수 출력
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다')

'''
첫 번째 짝수를 찾았습니다: 6
'''
```

- continue
> 현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감
```python
# 리스트에서 홀수만 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num, end=' ')

'''
1 3 5 7 9 
'''
```
#### _break와 continue의 남용은 코드의 가독성을 저하시킬 수 있음_

### List Comprehension
```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```
- 활용
```python
# 0~9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_list = []
for i in range(10):
    new_list.append(i)
print(new_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. List comprehension
new_list_2 = [i for i in range(10)]
print(new_list_2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
- 조건문 추가
```python
# 1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)
print(new_list)  # [1, 3, 5, 7, 9]

# 2. List comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1]
print(new_list_2)  # [1, 3, 5, 7, 9]
```
- 리스트를 생성하는 3가지 방법 비교
```python
# 정수 1,2,3을 가지는 새로운 리스트 만들기

numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)  # [1, 2, 3]

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)  # [1, 2, 3]

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)
```
#### _간편하지만 가독성이 좋지 않으므로 남용하지 말자_
```python
lst = [i if i % 2 == 1 else str(i) for i in range(10)]
print(lst)  # ['0', 1, '2', 3, '4', 5, '6', 7, '8', 9]
```

## 참고
### pass
1. 코드 작성중 미완성 부분
```python
def my_func():
    pass
```
2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
```python
if condition:
    pass # 아무런 동작도 수행하지 않음
else:
    # 다른 동작 수행
```
3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행

### enumerate
> enumerate(iterable, start=0)  
> - iterable 객체의 각 요소에 대해 '인덱스'와 함께 반환하는 내장 함수
```python
result = ['a', 'b', 'c']

print(enumerate(result))  # <enumerate object at 0x018FDFC8>
print(list(enumerate(result)))  # [(0, 'a'), (1, 'b'), (2, 'c')]

for index, elem in enumerate(result):
    print(index, elem, end=', ')  # 0 a, 1 b, 2 c,
```