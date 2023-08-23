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

# 8/8 강의

## 패턴 매칭
### 고지식한 패턴 검색 알고리즘(Brute Force)
```python
p = 'is'    # 찾을 패턴
t = 'This is a book'    # 전체 텍스트
M = len(p)      # 찾을 패턴의 길이
N = len(t)      # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0   # index t(찾을)
    j = 0   # index p(전체)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i - M     # 검색 성공
    else: return -1             # 검색 실패
```
### KMP 알고리즘

### 보이어-무어 알고리즘

### 시저 암호