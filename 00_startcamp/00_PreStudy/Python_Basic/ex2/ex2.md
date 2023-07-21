# 2. 제어구조
## 2.1 while
### 2.1.1 입력받은 숫자만큼 반복하기
> input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
단, while 문을 사용하세요.
```python
N = int(input())
n = 0
while n < N:
    print(f' {N}')
    n += 1
```

### 2.1.2 제곱표
>정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.
```python
N = int(input())
n = 1
while n <= N:
    print(f'{n} {n ** 2}')
    n += 1
```

### 2.1.3 얌체공
>고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.
```python
n = 1
h = 100
while n <= 10:
    h *= 3 / 5
    print(f'{n} {round(h, 4)}')
    n += 1
```

## 2.2 조건문(if-elif-else)
### 2.2.1 숫자 읽기(1~3)
> input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요. 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.
```python
word = {1 : '일', 2 : '이', 3 : '삼'}
N = int(input())
print(word[N])
```

### 2.2.2 나이에 따른 세대 구분 (1)
> input()으로 사용자의 나이를 입력받은 후, 다음 표의 어느 세대에 속하는지 출력하세요. 입출력 문구는 자유롭게 지으면 됩니다.
>- ~1924 : 가장 위대한 세대(The Greatest Generation)
>- 1925~1945 : 침묵 세대(The Silent Generation)
>- 1946~1964 : 베이비붐 세대(baby boomer)
>- 1965~1980 : X세대(Generation X)
>- 1981~1996 : 밀레니얼(millennial)
>- 1997~ : Z세대(Generation Z)
```python
year = int(input("What year were you born? "))
if year <= 1924:
    print("The Greatest Generation")
elif 1925 <= year <= 1945:
    print("The Silent Generation")
elif 1946 <= year <= 1964:
    print("baby boomer")
elif 1965<= year <= 1980:
    print("Generation X")
elif 1981 <= year <= 1996:
    print("millennial")
else: print("Generation Z")
```

### 2.2.3 단위 기호
> Kilo(k) / Mega(M) / Giga(G) / Tera(T) / Peta(P) / Exa(E) / Zetta(Z) / Yotta(Y)
```python
N = int(input())
result = str(N)
if N >= 1000000000000000000000000:
    result = str(N // 1000000000000000000000000) + 'Y'
elif N >= 1000000000000000000000:
    result = str(N // 1000000000000000000000) + 'Z'
elif N >= 1000000000000000000:
    result = str(N // 1000000000000000000) + 'E'
elif N >= 1000000000000000:
    result = str(N // 1000000000000000) + 'P'
elif N >= 1000000000000:
    result = str(N // 1000000000000) + 'T'
elif N >= 1000000000:
    result = str(N // 1000000000) + 'G'
elif N >= 1000000:
    result = str(N // 1000000) + 'M'
elif N >= 1000:
    result = str(N // 1000) + 'k'
elif N >= 0:
    pass
print(result)
```

### 2.2.4 양수만 덧셈하기
> input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가, 음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 파이썬 스크립트를 작성하세요.
```python
sum = 0
while True:
    N = int(input())
    if N < 0:
        break
    else: sum += N
print(sum)
```

### 2.2.5 윤년 판별하기
> 연도를 나타내는 정수를 입력으로 받아서 윤년인지 아닌지 출력하는 프로그램을 작성해 보세요.
```python
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
N = int(input())
is_leap_year(N)
if is_leap_year(N): print(f'{N}년은 윤년입니다.')
else: print(f'{N}년은 윤년이 아닙니다.')
```

### 2.2.7 나이에 따른 세대 구분 (2)
> 미국과 달리, 우리나라에서는 보통 1955~1963년생을 ‘베이비붐 세대’로 봅니다. 사용자가 한국인인지에 따라 세대를 구분할 수 있게 프로그램을 고쳐 보세요. (문제를 단순화하기 위해, 산업화 세대와 386 세대는 고려하지 않습니다. 그리고 사용자는 미국인 또는 한국인이라고 가정합니다.)
```python
def Generation(year):
    if year <= 1924:
        return "The Greatest Generation"
    elif year <= 1945:
        return "The Silent Generation"
    elif year <= 1964:
        if year <= 1954 or year == 1964:
            ans = input('Are you Korean?(y/n) ')
            if ans == 'y':
                if year <= 1954:
                    return "The Silent Generation"
                else:
                    return "Generation X"
            else:
                return "baby boomer"
        else:
            return "baby boomer"
    elif year <= 1980:
        return "Generation X"
    elif year <= 1996:
        return "millennial"
    else: 
        return "Generation Z"

when = int(input('What year were you born? '))
print(Generation(when))
```

## 2.3 for문
### 입력받은 숫자만큼 반복하기(for)
> input()으로 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다. 단, 이번에는 for 문을 사용하세요.
```python
num = int(input())
for i in range(num):
    print(f' {num}')
```

### 제곱표(for)
> 정수를 한 개 입력받아 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, 이번에는 for 문을 사용하세요.
```python
num = int(input())
for i in range(1, num + 1):
    print(f'{i} {i ** 2}')
```

### 화학실험
> 대학교의 화학자들은 상처를 매우 빠르게 치료하는 약물을 제조하는 새로운 과정을 개발했다. 제조 과정은 매우 길고 화학 약품을 매번 모니터링해야 하므로 몇 시간씩 걸린다! 학생들은 졸거나 딴짓을 하므로 이 일을 믿고 맏길 수가 없다. 그러므로 약물의 제조를 모니터링하는 자동 장치를 프로그래밍해야 한다. 장치는 15초마다 온도를 측정해 프로그램에 제공한다.
> 
> 프로그램은 먼저 최소와 최대의 안전 온도를 나타내는 두 개의 정수를 읽는다. 그 다음에, 장치가 제공하는 온도(정수)를 계속 읽는다. 화학 반응이 완료되면 장치는 끝을 알리는 -999를 보낸다. 기록된 온도가 올바른 범위에 있을 경우(최솟값 또는 최댓값과 같아도 된다) Nothing to report를 표시해야 한다. 하지만 온도가 위험 수준에 도달하면 Alert!를 표시하고 온도 측정을 중단한다(장치가 온도값을 계속 보내더라도).
```python
low, high = map(int, input().split())
datas = list(map(int, input().split()))

for data in datas:
    if low <= data <= high:
        print('Nothing to report')
    elif data == -999:
        break
    else:
        print('Alert!')
        break
```