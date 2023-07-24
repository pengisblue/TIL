# 7/24 강의
## Data Structure
> 여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dic ...)  
> == 자료구조
- 메서드를 호출하여 다양한 기능 활용하기

### 메서드(method)
> **객체**에 속한 함수
- 메서드는 class내부에 정의되는 함수
- 타입을 표현하는 방법
```python
print(help(list)) # 리스트 자료형에 대한 메서드를 확인할 수 있음
```
#### 메서드 호출 방법
```python
# 데이터 타입 객체.메서드()

print('hello'.capitalize())  # Hello

numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]
```

## Sequence Types
> 순서대로 나열하여 저장하는 자료형(str, list, tuple, range)
- 특징
    - Sequence(정렬X) / Indexing / Slicing / Length(len()) / Iteration

### 문자열
#### 조회/탐색 및 검증 메서드
|메서드|설명|
|:--:|:--|
|s.find(x)|x의 첫 번째 위치를 반환 없으면, -1을 반환|
|s.index(x)|x의 첫 번째 index값을 반환 없으면, 오류 발생|
|s.isalpha()|알파벳 문자 여부 <br>*단순 알파벳이 아닌 유니코드 상 Letter (한국어 포함)|
|s.isupper()|모든 문자 대문자 여부|
|s.islower()|모든 문자 소문자 여부|
|s.istitle()|타이틀 형식(첫 글자 대문자, 나머지 소문자) 여부|

#### 조작 메서드 (새 문자열 반환)
|메서드|설명|
|:--:|:--|
|s.replace(old, new[,count])|바꿀 대상 글자를 새로운 글자로 바꿔서 반환|
|s.strip([chars])|공백이나 특정 문자를 제거|
|**s.split**(sep=None, maxsplit=-1)|공백이나 특정 문자를 기준으로 문자열을 분리|
|'separator'.**join**([iterable])|구분자로 iterable을 합침|
|s.capitalize()|가장 첫 번째 글자를 대문자로 변경|
|s.title()|문자열 띄어쓰기 기준으로 각 단어 첫 글자는 대문자, 나머지는 소문자로 변경|
|s.upper()|모두 대문자로 변경|
|s.lowwer()|모두 소문자로 변경|
|s.swapcase()|대<->소문자 서로 변경|
```python
# 'separator'.join([iterable])
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # Hello-world!

#메서드는 이어서 사용 가능
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!
```

### 리스트
#### 값 추가 및 삭제 메서드
|메서드|설명|
|:--:|:--|
|**L.append(x)**|리스트 마지막 항목에 x를 추가|
|**L.extend(m)**|Iterable m의 모든 항목들을 리스트 끝에 추가 (+= 기능)|
|L.insert(i, x)|리스트 index i에 항목 x를 삽입|
|L.remove(x)|리스트 가장 왼쪽에 있는(첫 번째) x를 제거<br>항목이 존재하지 않을 경우, ValueError|
|**L.pop()**|리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거|
|L.pop(i)|리스트 index i에 있는 항목을 반환 후 제거|
|L.clear()|리스트의 모든 항목을 삭제|
```python
# .append(), .extend()
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

numbers.append(numbers2)
print(numbers)  # [1, 2, 3, [4, 5, 6]]

numbers.extend(numbers2)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# .pop()
lst = [1, 2, 3, 4, 5]

item1 = lst.pop()
item2 = lst.pop(0)

print(item1)  # 5
print(item2)  # 1
print(lst)  # [2, 3, 4]
```

### 탐색 및 정렬 메서드
|메서드|설명|
|:--:|:--|
|L.index(x, start, end)|리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 **index**를 반환|
|**L.reverse()**|리스트를 역순으로 변경(정렬 x)|
|**L.sort()**|원본 리스트를 정렬(매개변수 이용가능)|
|L.count(x)|리스트 항목 x의 개수를 반환|
```python
# .sort()
lst = [3, 2, 1]
lst.sort()
print(lst)  # [1, 2, 3]

# 내림차순
lst.sort(reverse=True)
print(lst)  # [3, 2, 1]
```
```python
# sort와 sorted
numbers = [3, 2, 1]
# sort 메서드
print(numbers.sort())  # None 원본 값을 바꾸고 return이 없음

numbers = [3, 2, 1]
# sorted 함수
print(sorted(numbers))  # [1, 2, 3]
print(numbers)  # [3, 2, 1]
```
```python
numbers = [1, 2, 3]

```
## 참고
### 문자열에 포함된 문자들의 유형을 판별하는 메서드
- isdecimal()
    - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- isdigit()
    - isdecimal()과 비슷하지만, 유니코드 숫자도 인식('①'도 숫자로 인식)
- insumerit()
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식(분수, 지수, 루트 기호도 숫자로 인식)