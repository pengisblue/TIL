# 7/17 강의
## 프로그래밍
> 명령어들의 집합 / 문제를 해결을 위한 방법

## 파이썬
### 파이썬 소개
- 간결하고 읽기 쉬운 문법
- 다양한 응용 분야

### 파이썬 실행
파이썬 - 파이썬 인터프리터 / 컴파일러 - 운영체제
1. shell을 사용하여 실행
```bash
$ python -i
$ # 명령어 입력
$ exit() # 종료
```
2. .py파일을 실행
```bash
$ python {파일명}.py
```
### 표현식과 값
1. 표현식
    - 값, 변수, 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조
평가: 표현식이나 문장을 실행하여 값을 결정
2. 문장
    - 실행 가능한 동작을 기술하는 코드 (조건문, 반복문, 함수 정의 등)
    - 문장은 여러개의 표현식을 포함

### 타입
> "값"과 "값에 적용할 수 있는 연산"
1. 값
    - Numeric Type : int, float, complex
    - Sequence Types : list, tuple, range
    - Text Sequence Type : str
    - Set Types : set
    - Mapping Types : dict
    - etc : None, Boolean, Funcitons

2. 연산자 ( -, +, -, *, /, //, %, ** )
    - 연산 우선 순위
        - ** > - (음수부호) > *, /, //, % > +, -
    ```python
    # -16
    -2 ** 4
    # -16
    -(2 ** 4)
    # 16
    (-2) ** 4
    ```

### 변수와 메모리
1. 변수
    - 값을 **참조**하는 이름
    - 변수명 규칙
        - 영문 알파벳, 언더스코어(_), 숫자로 구성
        - 숫자로 시작할 수 없음
        - 대소문자를 구분
        - 아래 키워드는 파이썬 내부 예약어로 사용할 수 없음
```python
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
2. 변수, 값 그리고 메모리

    메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재
    - 객체
        - 타입을 갖는 메모리 주소 내 값
        - "값이 들어있는 상자"
    - 변수는 그 변수가 참조하는 객체의 메모리 주소를 가짐
    ```python
    print(id({변수})) # 메모리 주소를 확인하는 법
    ```
    - 할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
    - 값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장
        - 존재하지 않는 변수: 새 변수를 생성
        - 기존에 존재했던 변수: 기존의 변수를 재사용해서 변수의 메모리 주소를 변경
    ```python
    number = 10
    double = 2 * number
    print(double) # 20

    number = 5
    print(double) # 20
    ``` 
## 읽기 좋은 코드
### [Style Guide](https://peps.python.org/pep-0008/)
> 코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장사항들의 모음
1. 변수명은 무엇을 위한 변수인지 직관적인 이름을 가져야 함
    - is로 시작하는 변수: True or False를 반환
    ```python
    temperature = 25
    is_hot = temperature > 30
    print(is_hot) # False
    ```
    - 변수의 단수 / 복수 표시
    ```python
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
    ```
    - 상수는 대문자로 표현
    ```python
    # 시간 예시
    seconds = 60
    minute = 60
    hours = 24
    
    SECONDS_PER_MINUTE = 60 # 이렇게 사용
    ```
2. 들여쓰기는 공백 4칸
3. 한 줄의 길이는 79자, 길어질 경우 줄바꿈(\)을 사용
4. 문자와 밑줄(_)을 사용하여 함수, 변수, 속성의 이름을 작성 *snake_case*
5. 함수 정의나 클래스 정의 등의 블록 사이에는 공백을 두 줄 추가
    ```python
    def sample():
      asdf
    
    
    def sample2():
      qwer
    ```
6. 연산자 사이를 띄워주기
    ```python
    result = 2+3*(4-5)/2
    result = 2 + 3 * (4 - 5) / 2 # 이렇게 사용
    ```

## 참고
### [Python Tutor](https://pythontutor.com/)
### 주석
- 코드의 특정 부분을 설명하거나 임시로 코드를 비활성화할 때 (~~미래의 나를 위해서~~)
```python
# 이것은
age = 10

# 주석입니다
print(age)

def sample():
  """
  이 함수는 ~ 함수입니다.
  
  예시)
  ...
  """
```