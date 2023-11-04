# 10/24 강의
> ECMAScript 2015(ES6) 이후의 명제를 따름<br>
[권장 스타일 가이드](https://standardjs.com/rules-kokr.html)

## 변수
### 식별자(변수명) 작성 규칙
- 문자, $, _ 로 시작
- 대소문자 구분
- 예약어 사용 불가
- 카멜 케이스(camelCase)
    - 변수, 객체, 함수에 사용
- 파스칼 케이스(PascalCase)
    - 클래스, 생성자 사용
- 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수에서 사용

### 변수 선언 키워드
- let
- const
- var

### let
- 블록 스코프를 갖는 지역 변수를 선언
- 재할당 가능
- 재선언 불가능
```javascript
let number = 10 // 선언 및 초기값 할당
number = 20 // 재할당
```
```javascript
let number = 10 // 선언 및 초기값 할당
// let number = 20 // 재선언 불가능
```

### const
- 블록 스코프를 갖는 지역 변수를 선언
- 재할당, 재선언 불가능
- 초기값 없이 선언 불가능
```javascript
const number = 10 // 선언 및 초기값 할당
// number = 10 // 재할당 불가능
```
```javascript
const number = 10 // 선언 및 초기값 할당
// const number = 20 // 재선언 불가능
```
```javascript
// const number // Missing initializer in const declaration
// 선언 시 반드시 초기값 설정 필요
```
### 블록 스코프 (block scope)
- if, for, 함수 등의 `중괄호({})내부`를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
```javascript
let x = 1

if (x === 1) {
    let x = 2
    console.log(x)  // 2
}

console.log(x)  // 1
```

### 정리
- 기본적으로 const 사용을 권장
- 재할당이 필요한 변수는 let으로 변경해서 사용

## 데이터 타입
- 원시 자료형(Primitive type)
    - Number, String, Boolean, undefined, null
    - 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
    - 변수에 할당될 때 값이 복사됨
        - 변수 간에 서로 영향을 미치지 않음
```javascript
const bar = 'bar'
console.log(bar) // bar

bar.toUpperCase()
console.log(bar) // bar
```
```javascript
let a = 10
let b = a
b = 20
console.log(a) // 10
console.log(b) // 20
```
- 참조 자료형(Reference type)
    - objects(object, Array, Function)
    - 객체의 주소가 저장되는 자료형(가변, 주소가 복사)
    - 객체를 생성하면 객체의 메모리 주소를 변수에 할당
        - 변수 간에 서로 영향을 미침
```javascript
const obj1 = { name: 'Alice', age: 30 }
const obj2 = obj1
obj2.age = 40

console.log(obj1.age) // 40
console.log(obj2.age) // 40
```

### 원시 자료형
- Number
    - 정수, 실수형 숫자를 표현하는 자료형
```javascript
const a =  10
const b = 2.998e8 // 2.998 * 10^8
const c = Infinity
const d = NaN // Nat a Number
```
- String
    - 텍스트 데이터를 표현하는 자료형
    - '+'연산을 사용해 문자열끼리 결합
- Template literals(템플릿 리터럴)
    - 파이썬의 f-string
    - Backtick(``)을 이용
    - 표현식은 '\$'와 '중괄호'로 표기 ( \${expression} )
    - ES6+ 부터 지원
```javascript
const age = 100
const message = `홍길동은 ${age}세 입니다.`
console.log(message) // 홍길동은 100세입니다.
```
- null
    - 변수의 값이 없음을 `의도적으로` 표현할 때 사용
- undefined
    - 변수 선언 이후 직접 값을 할당하지 않으면 `자동으로 할당됨`
```javascript
let a = null
let b

console.log(a) // null
console.log(b) // undefined

// '값이 없음'에 대한 표현이 2가지인 이유 - JavaScriipt의 설계 실수

typeof null         // "object" -> 설계 당시의 버그를 해결하지 않음(하위 호환 유지)
typeof undefined    // "undefined"
```
- Boolean
    - true / false
    - 조건문, 반복문에서 Boolean이 아닌 데이터 타입은 "자동 형변환 규칙에 따라" true 또는 false로 변환됨
#### 자동 형변환
|데이터 타입|false|true|
|:--:|:--:|:--:|
|undefined|항상 false|X|
|null|항상 false|X|
|Number|0, -0, NaN|나머지|
|String|빈 문자열|나머지|
 
## 연산자
### 할당 연산자
- =, +=, -=, *=, %=
### 증가 & 감소 연산자
- 증가 연산자 (++)
    - 피연산자를 1 증가 시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
- 감소 연산자 (--)
> += 또는 -=와 같이 더 명시적인 표현으로 작성하는 것을 권장
- 비교 연산자
- 동등 연산자 (==)
    - boolean 값을 반환
    - `암묵적 타입 변환`을 통해 `타입을 일치시킨 후` 같은 값인지 비교
    - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
```javascript
console.log('1' == 1) // true
console.log(0 == false) // true
```
- `일치 연산자 (===)`
    - 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지 비교
    - 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
    - `엄격한 비교` -> 암묵적 타입 변환 X
    - 특수한 경우를 제외하고 `일치 연산자 사용 권장` (동등 연산자X)
```javascript
console.log('1' === 1) // false
console.log(0 === false) // false
```
- 논리 연산자
    - &&, ||, !
    - 단축 평가 지원
```javascript
1 && 0 // 0
0 && 1 // 0
4 && 7 // 7
1 || 0 // 1
0 || 1 // 1
4 || 7 // 4
```

## 조건문
### if
- 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
```javascript
const func1 = function(number) {
    if (number > 50) {
        return 'Big'
    } else if (number === 50) {
        return 'Same'
    } else {
        return 'Small'
    }
}
```
### 삼항 연산자
```javascript
조건문 ? 조건문이 참일 경우 실행할 표현식 : 조건문이 거짓일 경우 실행할 표현식
```
```javascript
const func2 = function (number) {
    return number > 50 ? 'Yes' : 'No'
}
```

## 반복문
### while
```javascript
while (조건문) {
    // do something
}
```

### for
```javascript
for ([초기문]; [조건문]; [증감문]) {
    // do somthing
}
```

### for...in (object 순회)
- 객체(object)의 `열거 가능`한 속성(property)에 대해 반복
```javascript
for (variable in object) {
    statement
}
```
```javascript
const fruits = {
  a: 'apple',
  b: 'banana'
}

for (const property in fruits) {
  console.log(property) // a, b
  console.log(fruits[property]) // apple, banana
}
```

### for...of (Iterable 순회)
- `반복 가능`한 객체(배열, 문자열 등)에 대해 반복 -> 순서, 인덱스
```javascript
for (variable of iterable) {
    statement
}
```
```javascript
const numbers = [1, 2, 3, 4]

for (const number of numbers) {
    console.log(number) // 1, 2, 3, 4
}
```

### 배열과 for...in
- 배열의 인덱스는 정수 이름을 가진 열거 가능한 속성
- for...in은 정수가 아닌 이름과 속성을 포함하여 `열거 가능한 모든 속성을 반환`
- 내부적으로 for...in은 배열의 반복자 대신 `속성 열거`를 사용하기 때문에<br>
    `특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음`
- 인덱스의 순서가 중요한 `배열에서는 사용하지 않음`
- 배열에서는 `for`, `for...of`반복을 사용

### 반복문 사용 시 const 사용 여부
- for 문
    - 최초 정의한 초기문의 변수를 `"재할당"`하면서 사용하기 때문에 `const 사용 불가`
- for...in, for...of
    - 재할당이 아닌, 매 반복마다 다른 속성 이름이 변수에 지정되는 것
    - `const`를 사용해도 에러가 발생하지 않음
        - 단, const 특징에 따라 블록 내부에서는 변수 수정 불가

## 참고
### 세미콜론
- 선택적으로 사용 가능
- 세미콜론이 없으면 자동으로 삽입됨

### 변수 선언 키워드 - 'var'
- ES6 이전에 변수선언에 사용했던 키워드
- 재할당 & 재선언 가능
- "호이스팅"(변수를 선언 이전에 참조)되는 특징
- 함수 스코프(함수의 중괄호 내부)를 가짐
    - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능
    - 블록 스코프를 신경쓰지 않고 함수 스코프만 판단
- 변수 선언 시 키워드를 사용하지 않으면 자동으로 var로 선언 됨

### 함수 스코프
- 함수의 중괄호 내부
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

### 호이스팅(hoisting)
- 변수를 선언 이전에 참조할 수 있는 현상
    - 변수들은 실제 실행시에 코드의 최상단으로 끌어 올려지게 됨
- (var로 선언된 변수는) 변수 선언 이전의 위치에서 접근 시 undefined를 반환

### NaN을 반환하는 경우
1. 숫자로 읽을 수 없음(Number(undefined))
2. 결과가 허수인 수학 계산식 (Math.sqrt(-1))
3. 피연산자가 NaN (7 ** NaN)
4. 정의할 수 없는 계산식 (0 * Infinity)
5. 문자열을 포함하면서 덧셈이 아닌 계산식 ('가'/3)