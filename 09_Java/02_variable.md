# 변수
> `패키지(package)`
> - 자바 파일을 구분하기 위한 폴더
> - 자바 파일 첫 줄에 소속된 패키지를 선언해주어야한다.
> - 자바 파일이 위치하는 패키지와 package 선언 위치는 같아야 한다.
```java
package variable;

public class Var1 {
}
```

## 변수 시작
```java
package variable;

public class Var2 {
    public static void main(String[] args) {
        int a;  // 변수 선언
        a = 10; // 변수 초기화

        System.out.println(a);
        System.out.println(a);
        System.out.println(a);
    }
}

// 10
// 10
// 10
```
### 변수 선언
> `int a`
- 숫자 정수(integer)를 보관할 수 있는 이름이 a라는 데이터 저장소 = 변수
- 이제 a에는 숫자 정수를 보관할 수 있다.
- 문자, 소수와 같이 다양한 종류의 값을 저장할 수 있는 변수들이 있다.

### 변수 값에 대입
> `a = 10`
- 선언한 변수에 처음으로 값을 대입해서 저장하는 것을 변수 초기화라 한다.

### 변수 값 읽기
> `System.out.println(a)`

## 변수 값 변경
```java
int a;
a = 10;
System.out.println(a);  // 10
a = 50; // 변수 값 변경: a(10 -> 50)
System.out.println(a);  // 50
```

## 변수 선언과 초기화
### 변수 선언
```java
// 하나씩 선언할 수도 있고
int a;
int b;

// 한 번에 여러 변수를 선언할 수도 있다.
int c, d;
```

### 변수 초기화
```java
public static void main(String[] args) {
    // 1. 변수 선언, 초기화 각각 따로
    int a;
    a = 1;
    System.out.println(a);

    // 2. 변수 선언과 초기화를 한번에
    int b = 2;
    System.out.println(b);

    // 3. 여러 변수 선언과 초기화를 한번에
    int c = 3, d = 4;
    System.out.println(c);
    System.out.println(d);
}
```

### 변수는 초기화 해야한다.
```java
public static void main(String[] args) {
    int a;
    System.out.println(a);  // java: variable a might not have been initialized
}
```
> 지금 학습하는 변수는 지역 변수(Local Variable)라고 하는데, 지역 변수는 개발자가 직접 초기화를 해주어야 한다. 
> 나중에 배울 클래스 변수와 인스턴스 변수는 자바가 자동으로 초기화를 진행해준다.

## 변수 타입1
```java
public static void main(String[] args) {
    int a = 100; // 정수
    double b = 10.5; // 실수
    boolean c = true; // 불리언 true, false
    char d = 'A'; // 문자 하나
    String e = "Hello Java"; // 문자열, 문자열을 다루기 위한 특별한 타입

    System.out.println(a);  // 100
    System.out.println(b);  // 10.5
    System.out.println(c);  // true
    System.out.println(d);  // A
    System.out.println(e);  // Hello Java
}
```
- `int` : 정수를 다룬다. `1` , `100` , `1000`
- `double` : 실수를 다룬다. `0.2` , `1.5` , `100.121`
- `boolean` : 불리언 타입이라 한다. `true` , `false` 값만 사용할 수 있다. 주로 참과 거짓을 판단하는 곳에서 사용한다.
- `char` : 문자 하나를 다룰 때 사용한다. 작은따옴표( `'` )를 사용해서 감싸야 한다. `'A'` , `'가'`
- `String` : 문자열을 다룬다. 큰따옴표를 사용해야 한다. `"hello java"`

### 자신의 타입에 맞는 데이터 사용
- `int a = "백원"` : 정수 타입에 문자열(X)
- `int a = "100"` : 정수 타입에 문자열(X), 이것은 숫자 100이 아니라 문자열 `"100"` 이다. 문자를 나타내는 쌍따옴표( `"` )로 감싸져 있다.
- `int a = 100` : 정수 타입에 정수 100(O)

### 리터럴
코드에서 개발자가 직접 적은 `100` , `10.5` , `true` , `'A'` , `"Hello Java"` 와 같은 고정된 값을 프로그래밍 용어로
리터럴(literal)이라 한다.
```java
int a = 100; //정수 리터럴
double b = 10.5; //실수 리터럴
boolean c = true; //불리언 리터럴
char d = 'A'; //문자 하나 리터럴
String e = "Hello Java"; //문자열 리터럴
```
- 변수의 값은 변할 수 있지만 리터럴은 개발자가 직접 입력한 고정된 값이다. 따라서 리터럴 자체는 변하지 않는다.
> 리터럴(literal)이라는 단어의 어원이 문자 또는 글자를 의미한다.

## 변수 타입2
### 숫자 타입
```java
// 정수
byte b = 127; // -128 ~ 127
short s = 32767; // -32,768 ~ 32,767
int i = 2147483647; //-2,147,483,648 ~ 2,147,483,647 (약 20억)

//-9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
long l = 9223372036854775807L;

//실수
float f = 10.0f;
double d = 10.0;
```
- 정수형
    - `byte` : -128 ~ 127 (1byte, 2⁸)
    - `short` : -32,768 ~ 32,767 (2byte, 2¹⁶)
    - `int` : -2,147,483,648 ~ 2,147,483,647 (약 20억) (4byte, 2³²)
    - `long` : -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 (8byte, 2⁶⁴)
- 실수형
    - `float` : 대략 -3.4E38 ~ 3.4E38, 7자리 정밀도 (4byte, 2³²)
    - `double` : 대략 -1.7E308 ~ 1.7E308, 15자리 정밀도 (8byte, 2⁶⁴)

### 기타 타입
- `boolean` : `true` , `false` (1byte)
- `char` : 문자 하나(2byte)
- `String` : 문자열을 표현한다. 메모리 사용량은 문자 길이에 따라 동적으로 달라진다. (특별한 타입이다. 자세한 내용은 뒤에서 학습한다)

### 리터럴 타입 지정
- 정수 리터럴은 `int`를 기본으로 사용
    - 숫자가 int 범위를 넘어가면 `L`을 붙여서 `long`으로 변경해야 한다. (대문자 L 권장)
- 실수 리터럴은 `double`형을 기본으로 사용
    - `float`형을 사용하려면 `f`를 붙여서 float형으로 지정해야 한다.

## 변수 타입 정리
### 실무에서 거의 사용하지 않는 타입
- `byte`: 표현 길이가 너무 작다. `int`를 사용햐자.
    - 대신에 파일을 바이트 단위로 다루기 때문에 파일 전송, 파일 복사 등에 주로 사용된다.
- `short`: 표현 길이가 너무 작다. `int`를 사용햐자.
- `float`: 표현 길이와 정밀도가 낮다. 실수형은 `double` 을 사용하자.
- `char`: 문자 하나를 표현하는 일은 거의 없다. 문자 하나를 표현할 때도 문자열을 사용할 수 있다.
    - `String a = "b"` 와 같이 사용
> 메모리 용량은 매우 저렴하다. 메모리 용량보다 개발 속도나 효율에 초점을 맞추는 것이 효과적임

### 자주 사용하는 타입
- 정수 
    - `int`, `long`: 자바는 정수에 기본으로 `int`를 사용하고 만약 20억이 넘을 것 같으면 `long` 사용한다.
    - 파일을 다룰 때는 `byte` 를 사용
- 실수
    - `double`: 실수는 고민하지 말고 `double`을 쓰면 된다.
- 불린형 
    - `boolean` : `true` , `false` 참 거짓을 표현한다. 이후 조건문에서 자주 사용된다.
- 문자열
    - `String` : 문자를 다룰 때는 문자 하나든 문자열이든 모두 `String` 을 사용하는 것이 편리하다.

## 변수 명명 규칙
### 규칙
- 변수 이름은 숫자로 시작 X
- 공백 X
- 예약어 X
- 영문자, 숫자, 달러 기호 또는 밑줄만 사용

### 관례
- camel case를 사용
    - 소문자로 시작하고 여러 단어로 이루어진 경우 두 번째 단어부터 대문자로

### 자바 언어 관례
- 클래스는 대문자로 시작, 나머지는 소문자로 시작
- 예외
    - 상수는 모두 대문자를 사용하고 언더바로 구분
        - USER_LIMIT
    - 패키지는 모두 소문자
        - org.spring.boot
