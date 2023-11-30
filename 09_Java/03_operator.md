# 연산자
## 산술 연산자
### 연산자 종류
- 산술 연산자: `+` , `-` , `*` , `/` , `%` (나머지 연산자)
- 증감(증가 및 감소) 연산자: `++` , `--`
- 비교 연산자: `==` , `!=` , `>` , `<` , `>=` , `<=`
- 논리 연산자: `&&` (AND), `||` (OR), `!` (NOT)
- 대입 연산자: `=` , `+=` , `-=` , `*=` , `/=` , `%=`
- 삼항 연산자: `? :`

### 연산자와 피연산자
```
3 + 4
a + b
```
- 연산자(operator): 연산 기호 - `+` , `-`
- 피연산자(operand): 연산 대상 - `3` , `4` , `a` , `b`

### 산술 연산자
> 주로 숫자를 계산하는데 사용
- `+` (더하기)
- `-` (빼기)
- `*` (곱하기)
- `/` (나누기)
- `%` (나머지)
```java
// 변수 초기화
int a = 5;
int b = 2;

// 덧셈
int sum = a + b;
System.out.println("a + b = " + sum);   // a + b = 7

// 뺄셈
int diff = a - b;
System.out.println("a - b = " + diff);  // a - b = 5

// 곱셈
int multi = a * b;
System.out.println("a * b = " + multi);  // a * b = 10

// 나눗셈
int div = a / b;
System.out.println("a / b = " + div);  // a / b = 2

// 나머지
int mod = a % b;
System.out.println("a % b = " + mod);   // a % b = 1
```
