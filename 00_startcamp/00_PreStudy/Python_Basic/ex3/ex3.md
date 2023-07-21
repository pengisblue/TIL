# 3. 함수
## 3.1 함수
### 3.1.1 자릿수를 구하는 함수 만들기
> 양(陽)의 정수를 입력받아, 그 수가 몇 자리 숫자인지 출력하는 함수 numOfDigits()를 만들어 보세요.
```python
def numOfKigits(num):
    print(len(num))

number = input()
numOfKigits(number)
```

### 3.1.2 구구단
> 다음 예와 같이 구구단을 2단부터 9단까지 계산해서 출력하는 프로그램을 짜보세요.
>
> 2 * 1 = 2
>
> 2 * 2 = 4
>
> …        
>
> 9 * 9 = 81
```python
def gugu(num):
    for j in range(1, 10):
        print(f'{num} * {j} = {num * j}')
    print()


for i in range(2, 10):
    gugu(i)
```
### 3.2.1 숫자 읽기 함수(1~10)
> 매개변수로 받은 정수를 한국어로 표기한 문자열을 반환하는 함수 korean_number()를 정의하세요. 단, 매개변수는 1 이상 10 이하의 정수라고 가정합니다.
```python
def korean_number(num):
    korean = '일이삼사오육칠팔구십'
    return korean[num - 1]
```

### 3.2.3 이자(단리) 계산
> 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 이자를 구하는 함수 simple_interest()를 작성하세요.
```python
def simple_interest(principal, rate, time):
    return principal * rate * time
```
> 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 원리금을 계산하는 함수 simple_interest_amount()를 작성하세요.
```python
def simple_interest_amount(principal, rate, time):
    return principal * (1 + (rate * time))
```