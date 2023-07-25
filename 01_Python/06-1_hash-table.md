**해시 테이블 (Hash Table)**

- 데이터를 효율적으로 저장하고 검색하기 위해 사용되는 자료 구조

- 키-값 쌍을 연결하여 저장하는 방식

- 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
  - 이렇게 하면 데이터의 검색이 매우 빠르게 이루어짐

- 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장

- 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
- 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장

- 따라서 세트와 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음



**해시(Hash)**

- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
- 이렇게 생성된 고유한 값은 해당 데이터를 식별하는 데 사용될 수 있음
- 일종의 "지문"과 같은 역할
- 지문은 개인을 고유하게 식별하는 것처럼, 해시 값은 데이터를 고유하게 식별
- 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨



**set의 pop 메서드 예시**

- set에서 임의의 요소를 제거하고 반환

- 실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"가 아니라 "임의"라는 의미에서 "무작위"

  > By `"arbitrary"` the docs don't mean `"random"`

- 해시 테이블에 나타나는 순서대로 반환

```python
# 정수

my_set = {1, 2, 3, 9, 100, 4, 87, 39, 10, 52}

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)
```

> 정수 값 자체가 곧 해시 값



```python
# 문자열

my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}

print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
```

> 반환 값이 매번 다름



```python
print(hash(1))  # 1
print(hash(1))  # 1
print(hash('a'))  # 실행시마다 다름
print(hash('a'))  # 실행시마다 다름
```

- 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
- 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름
- 정수 타입의 경우, 정수 값 자체가 곧 해시 값이 됨
  - 즉, 같은 정수는 항상 같은 해시 값을 가짐
  - 해시 테이블에 정수를 저장할 때 효율적인 방법
  - 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨
- 반면에 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산
  - 이로 인해 문자열의 해시 값은 문자열의 내용에 따라 다르게 계산됨



**해시 함수**

- 주어진 객체의 해시 값을 계산하는 함수

- 해시 값은 객체의 고유한 식별자로 사용될 수 있으며, 해시 테이블과 같은 자료 구조에서 빠른 검색을 위해 사용됨

  ```python
  # TypeError: unhashable type: 'list'
  my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
  
  # TypeError: unhashable type: 'list
  my_dict = {[1, 2, 3]: 'a'}
  ```

  > `해시 가능성(hashable)`은 객체를 "딕셔너리의 키"나 "세트의 요소"로 사용할 수 있게 하는데, 이 자료 구조들이 내부적으로 해시 값을 사용하기 때문



**참고 문헌**

- https://docs.python.org/ko/3.9/library/stdtypes.html#set-types-set-frozenset
- https://docs.python.org/ko/3.9/glossary.html#term-hashable