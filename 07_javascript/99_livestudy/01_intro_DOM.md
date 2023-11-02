# 10/23 강의
## History of JavaScript
- 웹의 탄생 (1990)
    - 팀 버너스리 경이 WWW, 하이퍼텍스트 시스템 고안
    - URL, HTTP 최초 설계 및 구현
    - 초기의 웹은 정적인 텍스트 페이지만 지원
- 웹 브라우저의 대중화 (1993)
    - Netscape Navigator
- JavaScript의 탄생 (1995)
    - Netscape Navigator에 탑재되어 웹의 동적 기능을 추가
- JavaScript의 파편화 (1996)
    - JavaScript를 독자적으로 변경하고 자체 브라우저에 탑재
- 1차 브라우저 전쟁 (1995-2001)
    - 마이크로소프트는 IE를 윈도우 운영체제에 내장하여 무료 배포
- ECMAScript 출시 (1997)
    - JavaScript 표준 확립 시도
- 2차 브라우저 전쟁 (2004-2017)
    - Chrome의 등장으로 웹 표준의 중요성이 대두
    - 웹 애플리케이션의 발전

### ECMAScript
- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
    - ECMAScript는 언어의 핵심을 정의하고
    - JavaScript는 표준에 따라 구현된 언어로 사용됨

## JavaScript and DOM
### DOM
> The Document Object Model
- 웹페이지(Document)를 구조화된 객체로 제공
- 프로그래밍 언어가 페이지 구조에 접근하고 조작할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 변경

#### 특징
- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
- document 객체의 자식

#### DOM tree
- DOM tree라는 객체 트리로 구조화
    - 객체 간 상속 구조가 존재

## DOM 선택
### 선택 메서드
- document.`querySelector(CSS selector)`
    - 요소 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
- document.`querySelectorAll(CSS selector)`
    - 요소 여러 개 선택
    - 제공한 CSS selector를 만족하는 NodeList를 반환

## DOM 조작
### 속성(attribute) 조작
#### 클래스 속성 조작
- 요소의 클래스 목록을 DOMTokenList 형태로 반환
```
'classList' property
```

#### 일반 속성 조작

### HTML 콘텐츠 조작

### DOM 요소 조작

### style 조작
- 인라인 스타일로 적용
- 일반적으로는 css로 작성하고 클래스를 추가함

## 참고
### NodeList

### Element