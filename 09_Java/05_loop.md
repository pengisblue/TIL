# 반복문
## while문
> 조건에 따라 코드를 반복해서 실행
```java
while (조건식) {
    // 코드
}
```
### 연습 1
```java
public static void main(String[] args) {
    int count = 0;

    while (count < 3) {
        count++;
        System.out.println("현재 숫자는: " + count);
    }
}

// 현재 숫자는: 1
// 현재 숫자는: 2
// 현재 숫자는: 3
```

### 연습 2
- 1부터 하나씩 증가하는 수를 3번 더하기 (1 ~ 3 더하기)
```java
public static void main(String[] args) {
    int sum = 0;
    int i = 1;
    int endNum = 3;

    while (i <= endNum) {
        sum += i;
        System.out.println("i=" + i +  " sum=" + sum);
        i++;
    }
}

// i=1 sum=1
// i=2 sum=3
// i=3 sum=6
```

## do-while문
- while문과 비슷하지만, 조건에 상관없이 무조건 한 번은 코드를 실행한다.
```java
do {
    // 코드
} while (조건식);
```
### while문과 비교
```java
// while문

public static void main(String[] args) {
    int i = 10;
    while (i < 3) {
        System.out.println("현재 숫자는:" + i);
        i++;
    }
}

// 없음
```
```java
public static void main(String[] args) {
    int i = 10;
    do {
        System.out.println("현재 숫자는: " + i);
        i++;
    } while (i < 3);
}

// 현재 숫자는: 10
```

## break, continue
### break
```java
while (조건식) {
    코드1;
    break; // 즉시 while문 종료로 이동
    코드2;
}
// while문 종료
```
- `코드2`가 실행되지 않고 while문 종료

### continue
```java
while (조건식) {
    코드1;
    채ㅜ샤ㅜㅕㄷ; // 즉시 조건식으로 이동
    코드2;
}
```
- `코드2`가 실행되지 않고 다시 조건식으로 이동