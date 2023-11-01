# 11/01 강의
## Front-end Development
### Client-side frameworks
- Front-end Development?
    - 웹사이트와 웹애플리케이션의 UI와 UX를 만들고 디자인하는 것
    - HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호작용 하는 부분을 개발
- Client-side frameworks
    - 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임 워크

#### Client-side frameworks의 필요
- 웹에서 하는 일이 많아졌다.
    - 현대적이고 복잡한 대화영 웹사이트 `웹 애플리케이션`
- 다루는 데이터의 증가
    - 데이터를 안정적으로 추적하고 업데이트할 수 있어야함

### SPA (Single Page Application)
- 페이지 한 개로 구성된 웹 애플리케이션
- 동작
    1. 서버로부터 필요한 모든 정적 HTML을 처음에 한번 가져옴
    2. 브라우저가 페이지를 로드하면 Vue 프레임워크는 Ajax요청을 통해 데이터를 받아서 페이지의 일부 갱신
- 웹 애플리케이션의 초기 로딩 후, 새로운 페이지 요청 없이 <br>동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 애플리케이션
    - CSR (Client-side Rendering) 방식

#### CSR 방식
1. 브라우저는 페이지에 필요한 최소한의 HTML 페이지와 JavaScript를 다운로드
2. JavaScript를 사용하여 DOM을 업데이트하고 페이지를 렌더링

#### CSR 장점
1. 빠른 속도
    - 페이지의 일부를 다시 렌더링 할 수 있음
    - 서버로 전송되는 데이터의 양을 최소화
2. 사용자 경험
    - 새로고침이 발생하지 않아 네이티브 앱과 유사한 사용자 경험 제공
3. Front-end와 Back-end의 명확한 분리
    - Front-end는 UI 렌더링 및 사용자 상호 작용 처리
    - Back-end는 데이터 및 API 제공을 담당

#### CSR 단점
1. 초기 구동속도 느림
    - 전체 페이지를 보기 전에 약간의 지연
    - JavaScript가 다운로드, 구문 분석 및 실행될 때 까지 페이지가 완전히 렌더링되지 않음
2. SEO(검색 엔진 최적화)문제
    - 페이지를 나중에 그려 나가는 것이기 때문에 검색에 잘 노출되지 않을 수 있음

## Vue
- Why Vue?
    - 반응성 시스템
    - 모듈화 및 유연한 구조
        - 애플리케이션을 컴포넌트 조각으로 나눌 수 있음
- Vue의 핵심 기능
    1. 선언적 렌더링 (Declarative Rendering)
    2. 반응형 (Reactivity)

### Vue Tutorial
- Application instance
```json
const{ createApp } = Vue

cosnt app = creatApp({})
```
- ref()

## 참고
### Ref Unwrap 주의사항
- 템플릿의 unwrap은 ref가 최상위 속성인 경우에만 사용 가능