# 10/25 강의
## 함수
> 참조 자료형에 속하며 모든 함수는 Function object

### 함수 정의
- 함수 구조
    - 함수의 이름
    - 함수의 매개변수
    - 함수의 body를 구성하는 statement
    - return 값이 없다면 undefined를 반환
```javascript
function name ([param[, param,[ ..., param]]]) {
  statements
  return value
}
```

#### 선언식
- 익명함수 사용 불가
- 호이스팅 있음
```javascript
function funcName () {
  statements
}
```
```javascript
function add (num1, num2) {
  return num1 + num2
}

add(1, 2) // 3
```

#### 표현식 (권장)
- '익명 함수'를 사용할 수 있음
- 호이스팅 없음
```javascript
const funcName = funtion() {
  statements
}
```
```javascript
const sub = function (num1, num2) {
  return num1 - num2
}

sub(2, 1) // 1
```

### 매개변수
#### 매개변수 정의 방법
1. 기본 함수 매개변수
    - 값이 없고나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
```javascript
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

console.log(greeting()) // Hi Anonymous
```

2. 나머지 매개변수
    - 임의의 수의 인자를 `배열`로 허용하여 가변 인자를 나타내는 방법
    - 규칙
        - 함수 정의 시 나머지 매개변수 하나만 작성할 수 있음
        - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야함
```javascript
const myFunc = function (num1, num2, ...restArgs) {
  return [num1, num2, restArgs]
}

console.log(myFunc(1, 2, 3, 4, 5))  // [1, 2, [3, 4, 5]]
console.log(myFunc(1, 2))   // [1, 2, []]
```

#### 매개변수와 인자의 개수 불일치
- 매개변수 개수 > 인자 개수
    - 누락된 인자는 undefined로 할당
```javascript
const threeArgs = function (num1, num2, num3) {
  return [num1, num2, num3]
}

console.log(threeArgs())      // [undefined, undefined, undefined]
console.log(threeArgs(1))     // [1, undefined, undefined]
console.log(threeArgs(2, 3))  // [2, 3, undefined]
```

- 매개변수 개수 < 인자 개수
    - 초과 입력한 인자는 사용하지 않음
```javascript
const noArgs = function () {
  return 0
}

console.log(noArgs(1, 2, 3))    // 0

const twoArgs = function (num1, num2) {
  return [num1, num2]
}

console.log(twoArgs(1, 2, 3))   // [1, 2]
```

### Spread syntax '...' (전개구문)
- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)
- 전개 대상에 따라 역할이 다름
    - 배열이나 객체의 요소를 개별적인 값으로 분리
    - 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가
1. 함수와의 사용
    - 함수 호출 시 인자 확장
```javascript
function myFunc (x, y, z) {
    return x + y + z
}

let numbers = [1, 2, 3]

console.log(myFunc(...numbers)) // 6
```
    - 나머지 매개변수 (압축)
2. 객체와의 사용
3. 배열과의 사용

### 화살표 함수
- 함수 표현식의 간결한 표현법
```javascript
const arrow = function (name) {
    return `hello, ${name}`
}
```
```javascript
const arrow = name => `hello, ${name}`
```

#### 작성 과정
```javascript
// 1. function 키워드 삭제 & 화살표 작성
const arrow2 = (name) => { return `hello, ${name}` }

// 2. 인자가 1개일 경우: () 생략 가능 / 생략하지 않는 것을 권장
const arrow3 = name => { return `hello, ${name}` }

// 3. 함수 본문이 return을 포함한 표현식 1개일 경우: {} & return 삭제 가능
const arrow4 = name => `hello, ${name}`
```

## 참고
### 화살표 함수 심화
```javascript
// 1. 인자가 없다면 () or _ 로 표시 가능
const noArgs1 = () => 'No arges'
const noArgs2 = _ => 'No arges'

// 2-1. object를 return 한다면 return을 명시적으로 작성
const returnobj1 = () => {return { key: value }}

// 2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함
const returnobj2 = () => ({ key: value })
```

## 객체
> 키로 구분된 데이터 집합을 저장하는 자료형

### 구조 및 속성
#### 구조
- key는 문자형만 허용
- value는 모든 자료형 허용
```javascript
const user = {
  name: 'Alice',
  'key with space': true,
  greeting: function () {
    return 'hello'
  }
}
```

#### 속성 참조
- 점('.', chaining operator) 또는 대괄호([])로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
```javascript
// 조회
console.log(user.name) // Alice
console.log(user['key with space']) // true

// 추가
user.address = 'korea'
console.log(user) // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}

// 수정
user.name = 'Bella'
console.log(user.name) // Bella

// 삭제
delete user.name
console.log(user) // {key with space: true, address: 'korea', greeting: ƒ}

// in 연산자 (속성이 객체에 존재하는지 확인)
console.log('greeting' in user) // true
console.log('country' in user) // false

```

### 객체와 함수
- Method
    - 객체 속성에 정의된 함수
    - object.method() 방식으로 호출
    - 메서드는 객체를 '행동'할 수 있게 함
```javascript
// 메서드 호출
console.log(user.greeting()) // hello
```

### this
> 함수나 메서드를 호출한 객체를 가리키는 키워드
- 메서드는 `this` 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
- `함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정` (동적 할당)
```javascript
const user = {
  name: 'Alice',
  greeting: function () {
    return `Hello ${this.name}`
  }
}

console.log(user.greeting())  // Hello Alice
```

#### this의 대상
- 함수를 `"호출하는 방법"`에 따라 가리키는 대상이 다름
    - 단순 호출 : 전역 객체 (window)
    - 메서드 호출 : 메서드를 호출한 객체
```javascript
// 단순 호출
const myFunc = function () {
  return this
}

console.log(myFunc()) // Window

// 메서드 호출
const myObj = {
  data: 1,
  myFunc: function () {
  return this
  }
}

console.log(myObj.myFunc()) // myObj
```

#### 중첩된(Nested) 함수에서의 this 문제점과 해결책
- 문제점
```javascript
// for Each의 인자로 작성된 콜백 함수는 일반적인 함수 호출
// this는 전역 객체를 가리킴
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this, number)
      // window 1
      // window 2
      // window 3
    })
  }
}

console.log(myObj2.myFunc())
```
- 해결책
```javascript
// 화살표 함수는 자신만의 this를 가지지 않음
// 외부 함수에서 this를 가져옴
const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this)
      // myObj3
      // myObj3
      // myObj3
    })
  }
}

console.log(myObj3.myFunc())
```

### 추가 객체 문법
#### 1. 단축 속성
- key와 value의 이름이 같은 경우 단축 구문 사용 가능
```javascript
const name = 'Alice'
const age = 30
```
```javascript
const user = {
  name,   // name: name,
  age,    // age: age,
}
```

#### 2. 단축 메서드
- 메서드 선언 시 function 키워드 생략 가능
```javascript
const myObj = {
//  myFunc: function () {
    myFunc() {  
    return 'Hello'
  }
}
```

#### 3. 계산된 속성 (computed property name)
- 키가 대괄호([])로 둘러싸여 있는 속성
    - 고정된 값이 아닌 변수 값을 사용할 수 있음
```javascript
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix + suffix]: 'value',
}

console.log(bag) // {연필: 5, myproperty: 'value'}
```

#### 4. 구조 분해 할당 (destructing assignment)
- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

## 배열
- Object : 키로 구분된 데이터 집합을 저장하는 자료형
    - 순서가 없음
- Array : 순서가 있는 데이터 집합을 저장하는 자료구조

### 배열과 메서드
|메서드|역할|
|:--:|:--:|
|push()/pop()|배열 끝 요소를 추가/제거&반환|
|unshift()/shift()|배열 앞 요소를 추가/제거&반환|

### Array helper method
> 배열을 `순회`하며 `특정 로직을 수행`하는 메서드
- 메서드 호출 시 인자로 함수를 받는 것이 특징  

|메서드|역할|
|:--:|:--:|
|forEach|인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행|
|map|배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출하고,<br> 함수 호출 결과를 모아 `새로운 배열을 반환`|

> 콜백함수: 다른 함수에 인자로 전달되는 함수 

#### forEach()

#### map()