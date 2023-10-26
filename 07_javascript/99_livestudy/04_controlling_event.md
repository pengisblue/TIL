# 10/26강의
## 이벤트
- envent object
    - DOM에서 이벤트가 발생했을 때 생성되는 객체

### envent handler
#### .addEventListener()
- 특정 이벤트를 DOM요소가 수신할 때마다 콜백 함수를 호출
```javascript
// DOM요소.addEventListener(수신할 이벤트, 콜백함수)
// 콜백함수 -> 지정한 이벤트를 받아 할 일을 등록
EventTarget.addEventListener(type, handler)
```
- type
    - 수신할 이벤트 이름
    - 문자열로 작성
- handler
    - 발생한 event 객체를 수신하는 콜백 함수
    - 콜백함수는 발생한 Event object를 유일한 매개변수로 받음

- 버튼을 클릭하면 버튼 요소 출력하기
> 버튼에 이벤트 처리기를 부착하여 클릭 이벤트가 발생하면 이벤트가 발생한 버튼 정보를 출력

### 버블링
- 한 요소에서 이벤트가 발생하면, 

## 이벤트 핸들러 이용