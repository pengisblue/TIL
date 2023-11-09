# 11/9 강의
## Routing
- 네트워크에서 경로를 선택하는 프로세스
    - 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

### 개요

- routing이 없다면
    - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
    - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router
- Vue 프로젝트 생성 시 Router 추가
- Vue 프로젝트 구조 변화

### Basic Routing
- index.js에 라우터 관련 설정 작성 (주소, 이름, 컴포넌트)
- RouterLink의 'to' 속성으로 index.js에서 정의한 주소 속성 값(path)을 사용

### Named Routes
- 경로에 이름을 지정하는 라우팅

### Dynamic Route Matching with Params

### Programmatic Navigation

## Navigation Guard
- Vue router를 통해 특정 URL에 접근할 때

### Globally Guard
#### router.beforeEach()
- 다른 URL로 이동하기 직전에 실행되는 함수
- Global Before Guards
- return false
    - 현재 내비게이션을 취소
    - 브라우저 URL이 변경된 경우
- return Route Location
    - 경로 위치를 전달하여 다른 위치로 redirect
- `return이 없다면 'to' URL Route 객체로 이동`

#### router.beforeEnter()
- route에 진입했을 때만 실행되는 함수
    - 매개변수, 쿼리 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨

### In-component Guard
#### 컴포넌트 가드 종류
- onBeforeRouteLeave
    - 현재 라우트에서 다른 라우트로 이동하기 전에 실행
    - 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리

- onBeforeRouteUpdate
    - 이미 렌더링된 컴포넌트가 같은 라우트 내에서 업데이트되기 전에 실행
    - 라우트 업데이트 시 추가적인 로직을 처리

## 참고
### Lazy Loading Routes
- 첫 빌드 시 해당 컴포넌트를 로드 하지 않고,
- `해당 경로를 처음으로 방문할 때만 컴포넌트를 로드` 하는 것
    - 앱을 빌드할 때 앱의 크기에 따라 페이지 로드 시간이 길어질 수 있기 때문
- 기존 "정적 가져오기 방식"을 "동적 가져오기 방식"으로 변경하는 것과 같음