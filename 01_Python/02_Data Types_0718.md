# 7/18 강의
## Data Types
> 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정

## Numeric Types
### int
> 정수 자료형
- 진수 표현
    ```python
    print(0b10) # 2진수 2

    print (0o30) # 8진수 24

    print(0x10) # 16진수 16
    
    # 10진수 12를 2진수로
    print(bin(12)) # 0b1100

    print(oct(12)) # 0o14

    print(hex(12)) # 0xc
    ```

### flaot
> 실수 자료형 (실수에 대한 근삿값)
- 유한 정밀도
    ```python
    print(2 / 3) # 0.6666666666666666

    print(5 / 3) # 1.6666666666666667
    ```
- Floating point rounding error
    - math모듈을 사용하여 오류를 방지
- 지수 표현 방식 (10^)
    ```python
    number = 314e-2 # 314 * (10 ** (-2))

    print(type(number)) # float

    print(number) # 3.14
    ```

## Sequence Type
> 순서대로 나열하여 저장하는 자료형
> - 순서(Sequence) / 인덱싱(Indexing) / 슬라이싱(Slicing) / 길이(Length) / 반복(Iteration)
### str
- 중첩 따옴표
    ```python
    # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.
    print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.")

    # 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
    print('문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.')
    ```
- Escape sequence
    - \n(줄바꿈) \t(tap) \\(백슬래시) \'(작은 따옴표) \"(큰 따옴표)
    ```python
    # 철수야 '안녕'
    print('철수야 \'안녕\'')
  
    # 이 다음은 엔터
    # 입니다.
    print('이 다음은 엔터\n입니다.')
    ```

- String Interpolation
    > 문자열 안에 변수나 표현식을 삽입하는 방법
    ```python
    # f-string
    bugs = 'roaches'
    counts = 100
    area = 'living room'
    print(f'Debugging {bugs} {counts} {area}')
    # 참고
    # print('Debugging {} {} {}'.format(bugs, counts, area))
    # print('Debugging %s %d %s'%(bugs, counts, area))
    
    # f-string 응용
    greeting = 'hi'
    print(f'{greeting:>10}') # 오른쪽 정렬
    print(f'{greeting:^10}') # 가운데 정렬
    print(f'{3.141592:.4f}') # 소숫점 4째자리까지 반올림
    ```
- str은 불변
    - 새로운 문자열을 만들어서 문제 풀이
### list
- 어떠한 자료형도 저장할 수 있음
- list는 가변

### tuple
- 표현
    ```python
    tup = (1,) # 하나일 경우 ','가 있어야 튜플로 인식
    ```
- tuple은 불변
- 튜플은 '파이썬 내부 동작'에서 주로 사용됨

### range
- 연속된 정수 시퀀스
```python
range_1 = range(5)
range_2 = range(1, 10)

print(range_1) # range(0, 5)
print(range_2) # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능

print(list(range_1)) # [0, 1, 2, 3, 4]
print(list(range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
- range는 불변

## Non-sequence Types
### dict
> key - value 쌍으로 이루어진 순서와 중복이 없는 자료형
```python
dic1 = {}
```
- key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range)
- value는 모든 자료형 가능
    ```python
    dic = {'key' : 'value'}
    
    print(dic['key']) # value

    dic['key'] = 100 # 값변경
    print(dic) # {'key' : 100}
    ```
- dict은 가변

### set
> 순서와 중복이 없는 자료형
```python
set1 = set() # {}로 생성할 경우 dict이 됨
set2 = {1, 1, 1} # {1} 중복X
```
- 집합과 동일한 연산 처리 가능
    ```python
    set1 = {1, 2, 3}
    set2 = {3, 6, 9}

    # 합집합
    print(set1 | set2) # {1, 2, 3, 6, 9}

    # 차집합
    print(set1 - set2) # {1, 2}

    # 교집합
    print(set1 & set2) # {3}
    ```
- set는 가변

## Other Types
### None
> 값이 없음을 표현
```python
variable = None

print(variable) # None
```

### Boolean
> 비교 / 논리 연산의 평가 결과로 사용됨
- True / False

## Collection
>여러 개의 항목 또는 요소를 담는 자료 구조
    > - str, list, tuple, set, dict
### 불변과 가변
```python
my_str = 'hello'
my_str[0] = 'z' # TypeError: 'str' object does not support item assignment

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list) # [100, 2, 3]

# 불변 데이터
x = 10
y = x

x = 20
print(x) # 20
print(y) # 10

# 가변 데이터
list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1) # [100, 2, 3]
print(list_2) # [100, 2, 3]
```

## Type Conversion
### 암시적 형변환
> 파이썬이 자동으로 형변환을 하는 것
```python
print(3 + 5.0) # 8.0

print(True + 3) # 4

print(True + False) # 1
```

### 명시적 형변환
> 개발자가 직접 형변환을 하는 것 (형식에 맞게)

## 연산자
### 산술 연산자
> -(음수), +, -, *, /, //, %, **

### 복합 연산자
> +=, -=, *=, /=, //=, %=, **=

### 비교 연산자
> <, <=, >, >=, ==, !=, is, is not
- is 식별 연산자
    - ==는 동등성(equality), is는 식별성(identity)
    - is는 레퍼런스(주소)를 비교
    ```python
    print(2.0 == 2) # True

    print(2.0 is 2) # False
    ```

### 논리 연산자
> and, or, not
- 단축 평가 : 두 번째 피연산자를 평가하지 않고 결과를 결정
    - and, or 연산 시에 주의

### 맴버십 연산자
in
not in

### 시퀀스형 연산자
시퀀스형에서 '+'는 결합, '*'는 반복