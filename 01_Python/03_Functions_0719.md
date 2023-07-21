# 7/19 강의
## 함수
> 특정 자업을 수행하기 위한 재사용 가능한 코드 묶음
> - 함수 호출 : function_name(arguments)
### 내장 함수 (Built-in function)
[파이썬 공식문서](https://docs.python.org/ko/3.9/) - 라이브러리에서 확인 가능

### 함수구조
```python
def make_sum(pram1, pram2): # parameter (input)
    '''함수 설명 doc string
    >>> make_sum(1, 2)
    3
    '''
    return pram1 + pram2  # return value (output)
```

## 매개변수와 인자
> 매개변수 : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
>
> 인자 : 함수를 호출할 때, 실제로 전달되는 값
- Positional Arguments (위치인자) 
  : 함수 호출 시 인자의 위치에 따라 전달되는 인자
    - 위치 인자는 함수 호출 시 반드시 값을 전달해야함
    <br><br>
- Default Argument Values(기본 인자 값) 
  : 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 해당됨
    <br><br>
- Keyword Arguments (키워드 인자)
  : 함수 호출 시 인자의 이름과 값을 함께 전달하는 인자
    - 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함
    ```python
    def greeting(name, age):
        print(f'hello, {name}, {age}!')


    greeting('Joy', 22) # hello, Joy, 22!
    
    greeting(22, 'Joy') # hello, 22, Joy!
    
    greeting(age=22, name='Joy') # hello, Joy, 22!
    
    greeting(age=22, 'Joy') # positional argument follows keyword argument
    ```
    - 기본 인자 값이 있을 때
    ```python
    # print() 함수
    print('one', 'two', 3, end = '\t')  # end의 default값은 \n -> 키워드 인자로 변환
    ```
    <br>
- Arbitrary Argument Lists (임의의 인자 목록)
  : 정해지지 않은 개수의 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 '*'를 붙여 사용, 여러개의 인자를 tupule로 처리
    ```python
    def numbers(*args):
        print(args)


    numbers(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
    # 가변인자로 매개변수를 정의하면
    # 함수를 호출 할 때, N개의 값을 넘겨도 모두 하나의 변수에 할당
    # 모두 tuple로 묶어서 하나로 처리
    ```
    <br>
- Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
  : 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러개의 인자를 dictionary로 묶어 처리
    ```python
    def numbers(**kwargs):
        print(kwargs) 
        

    numbers(name='joy', age=30, address='Korea')  # {'name': 'joy', 'age': 30, 'address': 'Korea'}
    ```
    <br>
- 함수 인자 권장 작성 순서
    - 위치 > 기본 > 가변 > 가변 키워드
    
      *절대적인 규칙은 아니며, 상황에 따라 유연하게*
    ```python
    def func(pos1, pos2, default_arg='default', *args, **kwargs):
        ...
    ```
### Python의 범위(Scope)
> 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- 변수 수명주기(lifecycle)
    1. built-in scope
        - 파이썬이 실행된 이후부터 영원히 유지
    2. golbal scope
        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    3. local scope
        - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
<br><br>

- 이름 검색 규칙(Name Resolution)
    1. Local scope
    2. (Enclosed scope)
    3. Global scope
    4. Built-in scope

```python
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  # 10 2 500

    local(500)
    print(a, b, c)  # 10 2 3


enclosed()
print(a, b)  # 1 2
```
```python
age = 100

def parent_func():
    age = 30

    def child_func():
        age = 20
        print(age, 'child_func')

    child_func()  # 20
    print(age, 'parent_func')

parent_func()  # 30
print(age, 'global')  # 100
```
*함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음*
<br>

- 'global' 키워드
    - 변수의 스코프를 전역 범위로 지정하기 위해 사용
    - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
    ```python
    num = 0  # 전역 변수

    def increment():
        global num  # num를 전역 변수로 선언
        num += 1


    print(num)  # 0
    increment()
    print(num)  # 0
    ```
    - 주의사항
        - global키워드 선언 후에 접근
        - 매개변수에 global 사용 불가
        - 웬만하면 global말고 다른 방식으로 표현하자
        ```python
        global_var = '글로벌 값'

        def updat_value(global_var):  # 매개 변수 -> local scope
            print(global_var, '매개 변수로 받은 값')
            result = global_var * 3  # 글로벌 변수가 가지고 있던 값 활용 가능
            global_var = '로컬 값'  # 글로벌 변수에 할당된 값에 영향 없이 다른 값 재할당 가능
            return result

        print(updat_value(global_var))  # 인자로 global scope 변수를 넘김
        print(global_var)
        ```

### 재귀 함수
> 함수 내부에서 자기 자신을 호출 *(무한 호출 주의)*
- 종료 조건을 명확히(다른 값을 반환하도록), 반복되는 호출이 종료 조건을 향하도록

## 유용한 함수
### 유용한 내장 함수
1. map(function, iterable)
    - iterable의 모든 요소에 function을 적용하고, 그 결과를 map object로 변환
```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x014F9310>
print(list(result))  # ['1', '2', '3']

result = []
for number in numbers:
    result.append(str(number))

print(result)  # ['1', '2', '3']
``` 
```python
def some_func(parm1):
    return parm1 ** 2

print(some_func(3))  # 9
print(some_func)  # <function some_func at 0x01340388>

other_var = some_func
print(other_var(3))  # 9

numbers = [3, 6, 9]
print(list(map(other_var, numbers)))  # [9, 36, 81]

# map 함수 만들기
def my_map(func, iterable):
    for item in iterable:
        result = func(item)
        print(result, end=' ')

my_map(some_func, numbers)  # 9 36 81
```
<br>

2. zip(*iterables)
    - 임의의 iterable을 모아 tuple을 원소로 하는 zip object를 반환
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 24, 32]
cities = ['New York', 'London', 'Paris']

for name, age, city in zip(names, ages, cities):
    print(name, age, city)

'''
Alice 30 New York
Bob 24 London
Charlie 32 Paris
'''

# 두개의 리스트를 딕셔너리로 변환하기
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}
```

### lambda 함수
> 이름 없이 정의되고 사용되는 익명 함수
- 함수 구조
    - lambda 매개변수: 표현식
    ```python
    # 일반적인 함수 정의
    def addition(x, y):
        return x + y

    # lambda 함수 사용
    addition = lambda x, y: x + y  # 하지만 익명 함수를 이렇게 사용하지는 않음
    ```
```python
# map + lambda
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [2, 4, 6, 8, 10]
```

## Packing & Unpacking
### Packing
> 여러 개의 값을 하나의 변수에 tuple 묶어서 담는 것
        > 직접 사용하기보다는 파이썬 내부에서 사용함
- '*'을 활용한 패킹
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers  # *b는 남은 요소들을 리스트로 패킹하여 할당

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

### Unpacking
> 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
- '*'는 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹
- '**'는 딕셔너리 키-값 쌍을 함수의 키워드 인자로 언패킹 

## 모듈
> 한 파일로 묶인 변수와 함수의 모음 <br>
> 특정한 기능을 하는 코드가 작성된 .py

## 모듈 활용
### 모듈 가져오기
```python
import {모듈}

{모듈}.{변수/함수}
```
```python
from {모듈} import {변수}, {함수}
```
- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 마지막에 import된 이름으로 대체됨 
    - 'as'를 사용하여 별칭을 붙여줄 수 있음

### 사용자 정의 모듈
```python
import {파일명}  # 상대경로

my_func = {파일명}.{변수/함수}  # import한 파일에 있는 호출한 함수를 사용
```

## 파이썬 표준 라이브러리
### 패키지
```python
from {패키지} import {모듈}
```
- 외부 패키지
> pip를  사용하여 설치 후 import
```bash
$ pip install requests  # requests 외부 패키지 설치
```
```python
import requests  # requests를 import

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()

print(response)
```

