# 10/10 강의
## Database
#### 파일을 이용한 데이터 관리

#### 스프레드 시트를 이용한 데이터 관리

## Relational Database
### 데이터베이스 역할
- 데이터를 (구조적)`저장`하고 조작

### 관계형 데이터베이스
- 데이터 간에 `관계`가 있는 데이터 모음
- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
    - 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음 (데이터의 논리적 조작)
- 고객 데이터 간 비교
    - 각 데이터에 고유한 식별 값 부여(Primary Key)

#### 관계형 데이터베이스 관련 키워드
1. Table (aka Relation)
  - 데이터를 기록하는 곳
2. Field (aka Column, Attribute)
  - 데이터 타입이 지정됨
3. Record (aka Row, Tuple)
  - 데이터 값 저장
4. Database
  - 테이블의 집합
5. Primary Key
    - `레코드의 식별자`
6. Foreign Key (외래 키)
    - 다른 테이블의 레코드를 식별할 수 있는 키
    - 다른 테이블의 기본 키를 참조
    - 각 레코드에서 서로 다른 테이블 간의 `관계를 만드는 데` 사용

### DBMS
- 데이터베이스와 사용자 간의 `인터페이스` 역할
- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구등을 할 수 있도록 도움

### RDBMS
- Relational Database Management System

## SQL
- Structure Query Language
    - 테이블의 형태로 `구조화`된 관계형 데이터베이스에게 요청을 `질의(요청)`
- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

### SQL Syntax
```sql
SELECT column_name FROM table_name;
```
- SQL 키워드는 대소문자를 구분하지 않음
    - 하지만 대문자로 작성하는 것을 권장 (명시적 구분)
- 각 SQL Statements의 끝에는 세미콜론(;)이 필요
    - 세미콜론은 각 SQL Statements을 구분하는 방법 (명령어의 마침표)

### 수행 목적에 따른 SQL Statements의 4가지 유형
- DDL: 데이터의 기본 구조 및 형식 변경 - CREATE DROP ALTER
- **DQL**: 데이터 검색 - SELECT
- DML: 데이터 조작 - INSERT UPDATE DELETE
- DCL: 데이터 및 작업에 대한 사용자 권한 제어 - COMMIT ROLLBACK GRANT REVOKE

### SQL 표준
- 모든 RDBMS에서 SQL 표준을 지원
- 독자적 문법이 존재할 수 있음

## Querying data
### `SELECT` statement
```sql
SELECT
  select_list
FROM
  table_name;
-- SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
-- FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
```

### 정리
- SELECT문을 사용하여 테이블의 `데이터를 조회 및 반환`
- `*`을 사용하여 모든 데이터 조회 가능

## Sorting data
### ORDER BY statement
- 조회 결과의 레코드를 정렬
```sql
SELECT
  select_list
FROM
  table_name
ORDER BY
  column1 [ASC|DESC],
  column2 [ASC|DESC],
  ...;
```
- FROM clause 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본 값), 내림차순(DESC)으로 정렬
### Null값
- Null값이 존재할 경우 오름차순에서 Null값을 가장 먼저 정렬

## Filtering data
### `DISTINCT` statement
- 중복 제거
```sql
SELECT DISTINCT
  select_list
FROM
  table_name;
```

### `WHERE` statement
- 조회시 특정 검색 `조건`을 지정
```sql
SELECT
  select_list
FROM
  table_name
WHERE
  search_condition;
```

### Opertators
#### Comparison Opertators
#### Logical Opertators
#### `In` Opertators
#### `LIKE` Opertators
##### Wildcard Characters
- '%'
    - 0개 이상의 문자열과 일치하는지 확인
- '_'

### `LIMIT` clause
```sql
SELECT DISTINCT
  select_list
FROM
  table_name
LIMIT [offset,] row_count;
```

### `GROUP BY` clause
- 레코드를 그룹화하여 요약본 생성 ('집계 함수'와 함께 사용)
#### Aggregation Funcions(집계함수)

