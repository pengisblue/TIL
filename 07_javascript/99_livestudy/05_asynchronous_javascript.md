# 10/30 강의
## 비동기
### 동기(Synchronous)
- 프로그램의 실행 흐름이 순차적으로 진행
    - 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식

### 비동기(Asynchronous)
- 프로그램의 실행 흐름이 순차적이지 않으며, <br>
    작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식
    - 작업의 완료 여부를 신경 쓰지 않고 `동시에 다른 작업들을 수행할 수 있음`

### 특징
- 병렬젹 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 <br>
    응답이 빨리 오는 작업부터 처리

## JavaScript와 비동기
- Single Thread 언어 JavaScript

### JavaScript Runtime
- "JavaScript가 동작할 수 있는 환경(Runtime)"
- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와줄 환경 필요
    - `브라우저` 또는 `Node`와 같은 환경에서 처리

### 브라우저 환경에서의 
#### JavaScript 비동기 처리 관련 요소
1. JavaScript Engine의 `Call Stack`
2. `Web API`
3. `Task Queue`
4. `Event Loop`

#### 비동기 처리 동작 방식
1. 모든 작업은 `Call Stack`으로 들어간 수 처리
2. 오래걸리는 작업이 Call Stack으로 들어오면 `Web API`로 보내 별도로 처리하도록 한다.
3. Web API에서 처리가 끝난 작업들은 Call Stack으로 들어가지 못하고<br>
    `Task Queue`에 순서대로 들어간다
4. `Event Loop`가 Call Stack이 비어있는 것을 계속 체크하고<br>
    Call Stack이 빈다면 Task Queue에서 가장 먼저 처리되어 들어온(오래된) 작업을 Call Stack으로 보낸다.

#### 1. Call Stack

#### 2. Web API

#### 3. Task Queue (Callback Queue)

#### 4. Event Loop

### 정리

## AJAX
> Asynchronous JavaScript + XML
```
JavaScript의 비동기 구조와 XML 객체를 활용해
비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술
```
- 현재는 XML 보다 JSON을 더 많이 사용

#### XMLHttpRequest (XHR) 객체
- 서버와 상호작용할 때 사용하며 새로고침 없이도 URL에서 데이터를 가져올 수 있음
    - 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트
    - 주로 AJAX 프로그래밍에 많이 사용됨

#### 이벤트 핸들러

### Axios
- JavaScript에서 사용되는 HTTP 클라이언트 라이브러리
    - 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구

#### Axios 설치
- CDN사용
```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

#### Axios 구조
```javascript
```

#### 고양이 사진 가져오기

#### 정리
- axios는 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
    - 브라우저를 위해 XMLHttpRequest 생성
- 같은 방식으로 DRF로 만든 API 서버로 요청을 보내서 데이터를 받아온 후 처리할 수 있도록 함

## Callback과 Promise
### 비동기 콜백
#### 비동기 처리의 단점
- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라<br>
    `작업이 완료되는 순서에 따라 처리`한다는 것
- `코드의 실행 순서가 불명확`하다는 단점이 존재
    - 실행결과를 예상할 수 없다

#### 비동기 콜백

#### 비동기 콜백의 한계
- 콜백 지옥

### 프로미스
- JavaScript에서 비동기 작업의 결과(완료/실패)를 나타내는 객체
    - 비동기 작업이 완료되었을 때 결과 값을 반환하거나, <br>
        실패시 에러를 처리할 수 있는 기능을 제공
- 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- Promise 기반의 클라이언트 -> Axios 라이브러리
    - 성공에 대한 약속 `then()`
    - 실패에 대한 약속 `catch()`

#### 비동기 콜백 vs Promise

#### then & catch
- then(callback)
    - 요청한 작업이 성공하면 callback 실행
    - callback은 `이전 작업의 성공 결과를 인자`로 전달 받음
- catch(callback)
    - then()이 하나라도 실패하면 callback 실행
    - callback은 `이전 작업의 실패 객체를 인자로 전달 받음`
- than과 catch는 모두 항상 promise 객체를 반환
    - 계속해서 `chaining`할 수 있음

#### then 메서드 chaining의 목적
- 비동기 작업의 `순차적인` 처리 가능

## 참고
### 비동기를 사용하는 이유 - `사용자 경험`