# 조건문
## if문1 - if, else
### if문
```java
if (condition) {
    // 조건이 참일 때 실행되는 코드
}
```
> 코드 블록: {}(중괄호) 사이에 있는 코드
```java
public static void main(String[] args) {
    int age = 20; // 사용자 나이

    if (age >= 18) {
        System.out.println("성인입니다.");
    }

    if (age < 18) {
        System.out.println("미성년자입니다.");
    }
}

// 성인입니다.
```

### else문
```java
if (condition) {
    // 조건이 참일 때 실행되는 코드
} else {
    // 만족하는 조건이 없을 때 실행되는 코드
}
```
```java
public static void main(String[] args) {
    int age = 17;

    if (age >= 18) {
        System.out.println("성인입니다.");  // 참일 때 실행
    } else {
        System.out.println("미성년자입니다."); // 만족하는 조건이 없을 때 실행
    }
}

// 미성년자입니다.
```

## if문2 - else if
### else if
```java
if (condition1) {
    // 조건1이 참일 때 실행되는 코드
} else if (condition2) {
    // 조건1이 거짓이고, 조건2가 참일 때 실행되는 코드
} else if (condition3) {
    // 조건2이 거짓이고, 조건3이 참일 때 실행되는 코드
} else {
    // 모든 조건이 거짓일 때 실행되는 코드
}
```
- 예제
    - 7세 이하일 경우: "미취학"
    - 8세 이상 13세 이하일 경우: "초등학생"
    - 14세 이상 16세 이하일 경우: "중학생"
    - 17세 이상 19세 이하일 경우: "고등학생"
    - 20세 이상일 경우: "성인"
```java
int age = 14;

if (age <= 7) {
    System.out.println("미취학");
} else if (age <= 13) {
    System.out.println("초등학생");
} else if (age <= 16) {
    System.out.println("중학생");
} else if (age <= 19) {
    System.out.println("고등학생");
} else {
    System.out.println("성인");
}
```

## if문3 - if문과 else if 문
> 서로 관련이 없는 독립 조건이면 `else if`를 사용하지 않고 `if`문을 각각 따로 사용해야 한다.
- 예제
    - 아이템 가격이 10000원 이상일 때, 1000원 할인
    - 나이가 10살 이하일 때 1000원 할인
```java
// 각각의 if문
int price = 10000;
int age = 10;
int discount = 0;

if (price >= 10000) {
    discount = discount + 1000;
    System.out.println("10000원 이상 구매, 1000원 할인");
}

if (age <= 10) {
    discount = discount + 1000;
    System.out.println("어린이 1000원 할인");
}

System.out.println("총 할인 금액: " + discount + "원"); // 총 할인 금액: 2000원
```
```java
// if, else if문
int price = 10000;
int age = 10;
int discount = 0;

if (price >= 10000) {
    discount = discount + 1000;
    System.out.println("10000원 이상 구매, 1000원 할인");
} else if (age <= 10) {
    // 실행되지 않는다.
    discount = discount + 1000;
    System.out.println("어린이 1000원 할인");
} else {
    System.out.println("할인 없음");
}

System.out.println("총 할인 금액: " + discount + "원"); // 총 할인 금액: 1000원
```
- 상황에 따라 적절히 사용하자

### 참고 - if문 {} 중괄호 생략
- `if`문 다음에 실행할 명령이 하나만 있을 경우에는 `{}`중괄호를 생략할 수 있다. (`else if`, `else`도 마찬가지)
- 실행할 명령이 두개 이상인 경우에는 `{}`를 사용해야한다.
```java
if (false)
    System.out.println("1번");
    System.out.println("2번");

// 2번

// 두번째 줄이 실행 되는 이유는 중괄호가 없어서 첫 줄만 if문에 포함되기 때문
```
- 가독성과 유지보수성을 위해 `중괄호 사용을 권장`

## switch문
- 예제
    - 회원 등급(`grade`)에 따라 다음의 쿠폰을 발급해야 한다.
    - 1등급: 쿠폰 1000
    - 2등급: 쿠폰 2000
    - 3등급: 쿠폰 3000
    - 위의 등급이 아닐 경우: 쿠폰 500
```java
// if문을 사용한 코드
public static void main(String[] args) {
    int grade = 2;

    int coupon;
    if (grade == 1) {
        coupon = 1000;
    } else if (grade == 2) {
        coupon = 2000;
    } else if (grade == 3) {
        coupon = 3000;
    } else {
        coupon = 500;
    }
    System.out.println("발급받은 쿠폰 " + coupon); // 발급받은 쿠폰 2000
}
```

### switch 문
```java
switch (조건식) {
    case value1:
        // 조건식의 결과 값이 value1일 때 실행되는 코드
        break;
    case value2:
        // 조건식의 결과 값이 value2일 때 실행되는 코드
        break;
    default:
        // 조건식의 결과 값이 위의 어떤 값에도 해당하지 않을 때 실행되는 코드
    }
```
- 조건식의 결과 값이 어떤 `case`의 값과 일치하면 해당 `case`의 코드를 실행
- `break`문은 현재 실행 중인 코드를 끝내고 `switch`문을 빠져나가게 하는 역할
- 만약 `break`문이 없으면, 일치하는 `case`이후의 모든 `case`코드들이 순서대로 실행된다.
- `default`는 조건식의 결과값이 모든 `case`의 값과 일치하지 않을 때 실행된다. `if`문의 `else`와 같다.
- `default`구문은 선택이다.
- `if`, `else-if`, `else`구조와 동일하다.

```java
// 위의 예제를 switch문을 사용
public static void main(String[] args) {
    int grade = 2;

    int coupon;
    switch (grade) {
        case 1:
            coupon = 1000;
            break;
        case 2:
            coupon = 2000;
            break;
        case 3:
            coupon = 3000;
            break;
        default:
            coupon = 500;
    }
    System.out.println("발급받은 쿠폰 " + coupon); // 발급받은 쿠폰 2000
}
```
- break문이 없을 경우
```java
// break문이 없으면 다음 case도 실행 (break문을 만날 때 까지)
public static void main(String[] args) {
    int grade = 2;

    int coupon;
    switch (grade) {
        case 1:
            coupon = 1000;
            break;
        case 2:
            coupon = 2000;
            // 여기서 멈추지 않고 case3의 코드도 실행하게 된다.
        case 3:
            coupon = 3000;
            break;
        default:
            coupon = 500;
    }
    System.out.println("발급받은 쿠폰 " + coupon); // 발급받은 쿠폰 3000
}
```

### if문 vs switch문
- switch문은 참 거짓의 결과가 나오는 조건이 아닌 단순히 값만 넣을 수 있다.
- switch문은 조건식이 특정 case와 같은지만 체크할 수 있다. == 값이 같은지 확인하는 연산만 가능(문자도 가능)
- if문은 참 거짓의 결과가 나오는 조건식을 자유롭게 적을 수 있다.

### 자바 14 새로운 switch문
```java
public static void main(String[] args) {
    int grade = 2;

    int coupon = switch (grade) {
        case 1 -> 1000;
        case 2 -> 2000;
        case 3 -> 3000;
        default -> 500;
    };

    System.out.println("발급받은 쿠폰 " + coupon);
}
```

## 삼항 연산자
- if문에서 단순히 참과 거짓에 따라 특정 값을 구하는 경우
```java
// if문을 사용
public static void main(String[] args) {
    int age = 18;
    String status;
    if (age >= 18) {
        status = "성인";
    } else {
        status = "미성년자";
    }
    System.out.println("age = " + age + " status = " + status); // age = 18 status = 성인
}
```
```java
// 삼항연산자를 사용
public static void main(String[] args) {
    int age = 18;
    String status = (age >= 18) ? "성인" : "미성년자";
    System.out.println("age = " + age + " status = " + status); // age = 18 status = 성인
}
```

## 연습
### 문제1 : 학점 계산기
- 90점 이상: "A"
- 80점 이상 90점 미만: "B"
- 70점 이상 80점 미만: "C"
- 60점 이상 70점 미만: "D"
- 60점 미만: "F"
- 점수(`int score`)를 기반으로 학점을 출력
```java
public static void main(String[] args) {
    int score = 85;
    String grade;

    if (score >= 90) {
        grade = "A";
    } else if (score >= 80) {
        grade = "B";
    } else if (score >= 70) {
        grade = "C";
    } else if (score >= 60) {
        grade = "D";
    } else {
        grade = "F";
    }
    System.out.println("학점은 " + grade + "입니다.");
}
```

### 문제2 : 거리에 따른 운송 수단 선택하기
- 거리가 1km 이하이면: "도보"
- 거리가 10km 이하이면: "자전거"
- 거리가 100km 이하이면: "자동차"
- 거리가 100km 초과이면: "비행기"
- 거리(`int distance`)를 기반으로 운송 수단을 출력
```java
public static void main(String[] args) {
    int distance = 100;

    if (distance <= 1) {
        System.out.println("도보를 이용하세요");
    } else if (distance <= 10) {
        System.out.println("자전거를 이용하세요");
    } else if (distance <= 100) {
        System.out.println("자동차를 이용하세요");
    } else {
        System.out.println("비행기를 이용하세요");
    }
}
```

### 문제3 : 환율 계산하기
- 달러가 0미만이면: "잘못된 금액입니다."
- 달러가 0일 때: "환전할 금액이 없습니다."
- 달러가 0 초과일 때: "환전 금액은 (계산된 원화 금액)원입니다."
- 금액(`int dollar`)을 기반으로 한국 원으로의 환전 금액을 출력(환율: 1300원)
```java
public static void main(String[] args) {
    int dollar = 10;
    if (dollar < 0) {
        System.out.println("잘못된 금액입니다.");
    } else if (dollar == 0) {
        System.out.println("환전할 금액이 없습니다.");
    } else {
        int won = dollar * 1300;
        System.out.println("환전 금액은 " + won + "원입니다.");
    }
}
```

### 문제4 : 평점에 따른 영화 추천
- 요청한 평점 이상의 영화를 찾아서 추천하는 프로그램
    - 어바웃타임 - 평점9
    - 토이 스토리 - 평점8
    - 고질라 - 평점7
- 평점 변수는 `double rating`, `if`문 활용하기
```java
public static void main(String[] args) {
    double rating = 7.1;
    if (rating <= 9) {
        System.out.println("'어바웃타임'을 추천합니다.");
    }

    if (rating <= 8) {
        System.out.println("'토이 스토리'를 추천합니다.");
    }

    if (rating <= 7) {
        System.out.println("'고질라'를 추천합니다.");
    }
}
```

### 문제5 : 학점에 따른 성취도 출력하기
- `String grade`라는 문자열로 학점에 따라 성취도를 출력하는 프로그램
    - "A": "탁월한 성과입니다!"
    - "B": "좋은 성과입니다!"
    - "C": "준수한 성과입니다!"
    - "D": "향상이 필요합니다."
    - "F": "불합격입니다."
    - 나머지: "잘못된 학점입니다."
- `switch` 문 사용
```java
public static void main(String[] args) {
    String grade = "B";
    switch(grade) {
        case "A":
            System.out.println("탁월한 성과입니다!");
            break;
        case "B":
            System.out.println("좋은 성과입니다!");
            break;
        case "C":
            System.out.println("준수한 성과입니다!");
            break;
        case "D":
            System.out.println("향상이 필요합니다.");
            break;
        case "F":
            System.out.println("불합격입니다.");
            break;
        default:
            System.out.println("잘못된 학점입니다.");
    }
}
```

### 문제6: 더 큰 숫자 찾기
- `a`의 값은 `10`이고, `b`의 값은 `20`일 때, 삼항 연산자를 사용하여 두 숫자 중 더 큰 숫자를 출력하는 코드
```java
public static void main(String[] args) {
    int a = 10;
    int b = 20;
    int max = (a > b) ? a : b;
    System.out.println("더 큰 숫자는 " + max + "입니다.");
}
```