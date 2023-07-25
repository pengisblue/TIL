# 7/25 강의
## 비시퀀스 데이터 구조
### 1. set
#### 메서드
|메서드|설명|
|:--:|:--|
|s.add(x)|세트 s에 항목 x를 추가<br>이미 x가 있다면 변화 없음|
|s.clear()|세트 s의 모든 항목을 제거|
|s.remove(x)|세트 s에서 항목 x를 제거<br>항목 x가 없을 경우 Key error|
|s.pop()|세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거|
|s.discard(x)|세트 s에서 항목 x를 제거|
|s.update(iterable)|세트 s에 다른 iterable 요소를 추가|

#### 집합 메서드
|메서드|설명|연산자|
|:--:|:--:|:--:|
|set1.difference(set2)|set1 차집합 set2의 항목으로<br>세트를 생성 후 반환|set1 - set2|
|set1.intersection(set2)|set1와 set2의 교집합으로<br>세트를 생성 후 반환| set1 & set2|
|set1.union(set2)|set1와 set2의 합집합으로<br>세트를 생성 후 반환|set1 \| set2|
|set1.issubset(set2)|set1가 set2의 부분집합이면<br>True를 반환|set1 <= set2|
|set1.issuperset(set2)|set1가 set2의 포함집합이면<br>True를 반환|set1 >= set2|

### 2. dictionay
#### 메서드
|메서드|설명|
|:--:|:--|
|D.clear()|딕셔너리 D의 모든 키/값 쌍을 제거|
|D.get(k *[,default]*)|key k의 value를 반환 (key가 없으면 None이나 defalut값을 반환)|
|D.keys()|딕셔너리 D의 key를 모은 객체를 반환|
|D.values()|딕셔너리 D의 value를 모은 객체를 반환|
|D.items()|딕셔너리 D의 key/value 쌍을 모은 객체를 반환|
|D.pop(k *[,default]*)|딕셔너리 D에서 k를 제거하고 value 값을 반환<br>(key가 없으면 error나 defalut값을 반환)|
|D.setdefault(k *[,default]*)|딕셔너리 D에서 k의 value를 반환<br>(k가 D의 key가 아니면 k/None(default) 쌍을 D에 추가하고 v를 반환)|
|D.update(*[other]*)|other에 있는 각 key에 대해<br>D에 있는 key면 D의 key값(value)를 other의 value로 대체,<br>D에 없는 key면 key/value 쌍을 D에 추가|
```python
# [], .get(), .setdeafault()
# 혈액형 인원수 세기
# 결과: {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'AB']

# []
new_dict = {}
# blood_types을 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict:
        # 기존에 키의 값을 +1 증가
          new_dict[blood_type] += 1
    # 키가 존재하지 않는다면 (처음 설정되는 키)
    else:
         new_dict[blood_type] = 1
print(new_dict)

# .get()
new_dict = {}
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)

# .setdefalut()
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)
```

## 복사
### 데이터 타입과 복사
- "불변 데이터 타입"과 "가변 데이터 타입"의 복사가 다름
### 복사 유형
#### 1. 할당 (Assignment)
- 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
```python
numbers = [1, 2, 3]
list1 = numbers  # 할당
numbers[0] = 100
print(list1)  # [100, 2, 3]
```

#### 2. 얕은 복사
```python
a = [1, 2, 3]
# 슬라이싱
b = a[:]
print(a, b) # [1, 2, 3] [1, 2, 3]

b[0] = 100
print(a, b) # [1, 2, 3] [100, 2, 3]

# copy
c = a.copy()
c[0] = 100
print(a, c) # [1, 2, 3] [100, 2, 3]

# 얕은 복사의 한계
a = [1, 2, [1, 2]]
b = a[:]
b[2][0] = 100
print(a, b) # [1, 2, [100, 2]] [1, 2, [100, 2]]

a = [1, 2, [1, 2]]
c = a.copy()
c[2][0] = 999
print(a, c) # [1, 2, [999, 2]] [1, 2, [999, 2]]
```

#### 3. 깊은 복사
```python
import copy

original_list = [1, 2, [1, 2]]

deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list)  # [1, 2, [1, 2]] [1, 2, [999, 2]]
```