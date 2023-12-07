# 스코프
## 지역변수와 스코프
> 지금까지 학습한 변수들은 모두 지역 변수(Local Variable)로 그 특정 지역을 벗어나면 사용할 수 없다. 변수가 선언된 코드 블록(`{}`)이 지역을 의미한다. 지역 변수는 자신이 선언된 코드 블록(`{}`) 안에서만 생존하고, 코드 블록을 벗어나면 제거된다.

### main{}과 if{}
```java
public static void main(String[] args) {
    int m = 10; // m 생존 시작
    if (true) {
        int x = 20; // x 생존 시작
        System.out.println("if m = " + m); // 블록 내부에서 블록 외부는 접근 가능
        System.out.println("if x = " + x);
    } // x 생존 종료

    // System.out.println("main x = " + x); // 오류 변수 x 접근 불가
    System.out.println("main m = " + m);
} // m 생존 종료
```
- `int m`
    - `main{}` 코드 블록 안에서 선언, `main{}` 코드 블록이 종료될 때 까지 생존
    - `if{}` 블록 내부에서도 외부 블록에서 선언된 `m`에 접근 가능
- `int x`
    - `if{}` 코드 블록 안에서 선언, `if{}` 코드 블록이 종료될 때 까지 생존
    - `if{}` 코드 블록이 끝나면 `x`는 제거 -> 이후에 접근하면 `cannot find symbol` 오류 발생

**변수의 접근 가능한 범위를 스코프(Scope)라고 한다.**

### for{}
```java
public static void main(String[] args) {
    int m = 10;
    for (int i = 0; i < 2; i++) { // 블록 내부, for문 내
        System.out.println("for m = " + m); // 블록 내부에서 외부는 접근 가능
        System.out.println("for i = " + i);
    } // i 생존 종료

    // System.out.println("main i = " + i); // cannot find symbol
    System.out.println("main m = " + m);
}
```
- 초기식에 선언된 변수(`i`)는 `for`문 코드 블록 안에서만 사용 가능

## 스코프 존재 이유
```java
public static void main(String[] args) {
    int m = 10;
    int temp = 0;
    if (m > 0) {
        temp = m * 2;
        System.out.println("temp = " + temp);
    }
    System.out.println("m = " + m);
}
```
- `if{}`에서 사용하는 임시 변수 `temp`를 `main{}`에서 선언했을 때 발생하는 문제
    - 비효율적인 메모리 사용
        - `temp` 는 `if` 코드 블록에서만 필요하지만, `main()` 코드 블록이 종료될 때 까지 메모리에 유지됨
        - `if` 코드 블록 안에 `temp` 를 선언했다면 `if` 코드 블록의 종료 시점에 이 변수를 메모리에서 제거해서 더 효율적으로 메모리를 사용할 수 있다.
    - 코드 복잡성 증가
        - `if` 코드 블록이 끝나도 `main()` 어디서나 `temp` 를 여전히 접근할 수 있어서 신경써야한다.
- 수정된 코드
    ```java
    public static void main(String[] args) {
        int m = 10;
        if (m > 0) {
            int temp = m * 2;
            System.out.println("temp = " + temp);
        }
        System.out.println("m = " + m);
    }
    ```

### while vs for - 스코프 관점
**while**
```java
public static void main(String[] args) {
    int sum = 0;
    int i = 1;
    int endNum = 3;

    while (i <= endNum) {
        sum = sum + i;
        System.out.println("i=" + i + " sum=" + sum);
        i++;
    }
    //... 아래에 더 많은 코드들이 있다고 가정
}
```
**For**
```java
public static void main(String[] args) {
    int sum = 0;
    int endNum = 3;

    for (int i = 1; i <= endNum; i++) {
        sum = sum + i;
        System.out.println("i=" + i + " sum=" + sum);
    }
    //... 아래에 더 많은 코드들이 있다고 가정
}
```
- 스코프 관점에서 카운터 변수 `i`의 비교
    - `while`문에서 변수 `i`의 스코프: `main()`메서드 전체
    - `for`문에서 변수 `i`의 스코프: `for`문 안으로 한정
- 변수 `i`와 같이 `for`문 안에서만 사용되는 카운터 변수가 있다면<br>`for`문을 사용해서 스코프의 범위를 제한하는 것이 메모리 사용과 유지보수 관점에서 더 좋다.

# 형변환
## 자동 형변환
### 형변환
- 작은 범위에서 큰 범위로는 당연히 값을 넣을 수 있다.
- 큰 범위에서 작은 범위는 문제가 발생할 수 있다
    - 소수점 버림
    - 오버플로우

### 작은 범위에서 큰 범위 대입
> `int` < `long` < `double`
```java
public static void main(String[] args) {
    int intValue = 10;
    long longValue;
    double doubleValue;

    longValue = intValue; // int -> long
    System.out.println("longValue = " + longValue); // longValue = 10

    doubleValue = intValue; // int -> double
    System.out.println("doubleValue1 = " + doubleValue); // doubleValue1 = 10.0
    doubleValue = 20L; // long -> double
    System.out.println("doubleValue2 = " + doubleValue); // doubleValue2 = 20.0
}
```

### 자동 형변환
- 동작
```java
// intValue = 10
doubleValue = intValue
doubleValue = (double) intValue //형 맞추기
doubleValue = (double) 10 //변수 값 읽기
doubleValue = 10.0 //형변환
```