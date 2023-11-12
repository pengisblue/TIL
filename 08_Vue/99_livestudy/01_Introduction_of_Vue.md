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
    - 현대적이고 복잡한 대화형 웹사이트 `웹 애플리케이션`
- 다루는 데이터의 증가
    - `애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 업데이트해야 한다는 것`
    - 데이터를 안정적으로 추적하고 업데이트할 수 있어야함

### SPA (Single Page Application)
- 페이지 한 개로 구성된 웹 애플리케이션
- 동작
    1. 서버로부터 필요한 모든 정적 HTML을 처음에 한번 가져옴
    2. 브라우저가 페이지를 로드하면 Vue 프레임워크는 Ajax요청을 통해 데이터를 받아서 페이지의 일부 갱신
- 웹 애플리케이션의 초기 로딩 후, 새로운 페이지 요청 없이 <br>동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 애플리케이션
    - CSR (Client-side Rendering) 방식

#### CSR 방식
- 클라이언트에서 화면을 렌더링하는 방식
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
    - 쉽고 간편하다
    - 반응성 시스템
        - 데이터 변경에 따라 자동으로 화면이 업데이트 됨
    - 모듈화 및 유연한 구조
        - 애플리케이션을 컴포넌트 조각으로 나눌 수 있음
        - 코드의 재사용성을 높이고 유지보수를 용이하게 함
- Vue의 핵심 기능
    1. 선언적 렌더링 (Declarative Rendering)
        - 템플릿 구문을 사용하여 HTML이 JavaScript 데이터를 기반으로 어떻게 보이는지 설명할 수 있음
    2. 반응형 (Reactivity)
        - JavaScript 상태 변경사항을 자동으로 추적하고 변경사항이 발생할 때 DOM을 효율적으로 업데이트

### Vue Tutorial
#### CDN 방식
```html
<div id="app"></div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const{ createApp } = Vue
  
  // Application instansce
  // createApp은 객체를 가짐
  cosnt app = creatApp({})
  
  app.mount('#app')
</script>
```
#### Vue 기본 구조
- createApp()에서 전달된느 객체는 Vue 컴포넌트
- 컴포넌트의 상태는 setup() 함수 내에서 선언되어야 하며 `객체를 반환`
- 반환된 객체의 속성은 템플릿에서 사용할 수 있음
- 콧수염 구문({{ }})을 사용하여 메시지 값을 기반으로 동적 텍스트를 렌더링
- 콘텐츠는 JavaScript 표현식을 사용할 수 있음

#### ref()
- 반응형 상태(데이터)를 선언하는 함수
- 인자를 받아 .value 속성이 있는 ref 객체로 래핑(wrapping)하여 반환
- ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트
- 인자는 어떠한 타입도 가능
- 템플릿의 참조에 접근하려면 setup 함수에서 선언 및 반환 필요
```javascript
const { createApp, ref } = Vue

const app = createApp({
  setup() {
  // ref()를 사용해야 반응형 데이터가 됨
  const message = ref('hello vue!')
  console.log(message)  // ref 객체
  console.log(message.value)  //hello vue!
  return {
      message,
    }
  }
})
```
- 템플릿에서는 .value를 사용하지 않음 automatically unwrapped
```html
<div id="app">
  <h1>{{ message }}</h1>
  <!-- unwrapped되어서 .value로 접근X -->
  <!-- <h1>{{ message.value }}</h1>   -->
</div>
```

## 참고
### Ref Unwrap 주의사항
- 템플릿의 unwrap은 ref가 최상위 속성인 경우에만 사용 가능
```javascript
cosnt object = { id: ref(0) }
```
```html
{{ object.id + 1 }} <!-- [object Object]1 -->
<!-- object는 최상위 속성이지만 object.id는 그렇지 않음 -->
<!-- 표현식을 평가할 때 object.id가 unwrap 되지 않고 ref 객체로 남아있음 -->
```

### Why Refs?
- Vue는 템플릿에서 ref를 사용하고 나중에 ref의 값을 변경하면 자동으로 변경 사항을 ㄱ마지하고 그에 따라 DOM을 업데이트("의존성 추적 기반의 반응형 시스템")
- Vue는 렌더링 중에 사용된 모든 ref를 추적하며, 나중에 ref가 변경되면 이를 추적하는 구성 요소에 대해 다시 렌더링
 - JavaScript에서는 일반 변수의 접근 또는 변형을 감지할 방법이 없기 때문

 ### SEO (Search Engin Optimization)
 - google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 노출되도록 개선하는 과정을 일컫는 작업
 - 정보의 대상은 주로 HTML에 작성된 내용
 - 검색
    - 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
- 검색 엔진
    - 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
- 최근 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
    - SPA 서비스도 겁색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전 중

### CSR & SSR
- CSR과 SSR 중에 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
- SPA 서비스의 SSR을 지원하는 Framework
    - Vue의 Nuxt.js
    - React의 Next.js
    - Angular Universal