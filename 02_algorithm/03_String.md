# 8/7 강의
## 문자열
- 연결(Concatenation)
    - 문자열 + 문자열
- 반복
    - 문자열 * 수
- 문자열은 시퀀스 자료형으로 분류, 인덱스, 슬라이싱 연산들 사용
- 제공되는 메소드
    - replace(), split(), isalpha(), find()
- immutable

### 문자열 뒤집기
```python
s = 'Reverse'
s_lst = list(s)
N = len(s)
for i in range(N//2):
    s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]
print(''.join(s_lst))
print(s)
```

### 문자열 비교
```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1, s2, s5)   # abc abc abc
if s1 == s5:
    print('s1 == s5')
else:
    print('s1 != s5')
# s1 == s5  

if s1 is s5:
    print('s1 is s5')
else:
    print('s1 is not s5')
# s1 is not s5
```

### 문자열 숫자를 정수로 변환하기

### 문자열을 숫자를 정수로 변환하기
