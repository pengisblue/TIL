# day4 (1월 11일) 학습

## Hooks
### useState()
- state를 사용하기 위한 Hook
```jsx
const [변수명, set함수명] = useState(초기값);
// 변수 각각에 대해 set함수가 따로 존재
```
```jsx
import React, { useState } from "react";

function Counter(props) {
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>총 {count}번 클릭했습니다.</p>
            <button onClick={() => setCount(count + 1)}>
                클릭
            </button>
        </div>
    );
}
```

### useEffect()
- Side effect를 수행하기 위한 Hook
    - side effect: 다른 컴포넌트에 영향을 미칠 수 있는 작업, 렌더링 중에는 완료X 렌더링 이후에 작업
```jsx
useEffect(이펙트 함수, 의존성 배열);
```
```jsx
// Effect function이 mount, unmount 시에 단 한 번씩만 실행됨
useEffect(이펙트 함수, []);

// 의존성 배열을 생략하면 업데이트 될 때마다 호출
```
- 예시
```jsx
import React, { useState, useEffect } from "react";

function Counter(props) {
    const [count, setCount] = useState(0);

    // componentDidMount, componentDidUpdate와 비슷하게 작동
    useEffect(() => {
        // 브라우저 API를 사용해서 document의 title을 업데이트
        document.title = `You clicked ${count} times`;
    });

    return (
        <div>
            <p>총 {count}번 클릭했습니다.</p>
            <button onClick={() => setCount(count + 1)}>
                클릭
            </button>
        </div>
    );
}
```
```jsx
import React, { useState, useEffect } from "react";

function UserStatus(props) {
    const [isOnline, setIsOnline] = useState(null);

    function handleStatusChange(status) {
        setIsOnline(status.isOnline);
    }

    useEffect(() => {
        serverAPI.subscribeUserStatus(props.user.id, handleStatusChange);
        return () => {  // 컴포넌트가 unmount될 때 호출됨
            ServerAPI.unsubscribeUserStatus(props.user.id, handleStatusChange);
        };
    });

    if (isOnline === null) {
        return '대기 중...';
    }
    return isOnline ? '온라인' : '오프라인';
}
```
- 정리
```jsx
useEffect(() => {
    // 컴포넌트가 마운트 된 이후,
    // 의존성 배열에 있는 변수들 중 하나라도 값이 변경되었을 때 실행됨
    // 의존성 배열에 빈 배열([])을 넣으면 마운트와 언마운트시에 단 한 번씩만 실행됨
    // 의존성 배열 생략 시 컴포넌트 업데이트 시마다 실행됨
    ...

    return () => {
        // 컴포넌트가 마운트 해제되기 전에 실행됨
        ...
    }
}, [의존성 변수1, 의존성 변수2, ...]);
```

### useMemeo()
- Memoize value를 리턴하는 Hook
- computed와 유사한 개념?
```jsx
const memoizedValue = useMemo(
    () => {
        // 연산량이 높은 작업을 수행하여 결과를 반환
        return computeExpensiveValue(의존성 변수1, 의존성 변수2);
    },
    [의존성 변수1, 의존성 변수2]
);
```
- 의존성 배열의 값이 변했을 때에만 새로운 create함수를 호출하여 결과 값을 반환, 그렇지 않을 경우 기존 값 반환
    - 빠른 렌더링 가능
- 렌더링이 일어나는 동안 실행되는 작업
    - useEffect()와 구분해서 사용해야한다
```jsx
// 의존성 배열을 넣지 않으면 렌더링 마다 함수가 실행되므로 의미 X
const memoizedValue = useMemo(
    () => computeExpensiveValue(a, b);
);
```
```jsx
// 의존성 배열이 빈 배열일 경우, 컴포넌트 마운트 시에만 호출 됨 -> 마운트 이후에 값 변경 X
const memoizedValue = useMemo(
    () => {
        return computeExpensiveValue(a, b);
    },
    []
);
```

### useCallback()
- useMemo() Hook과 유사하지만 값이 아닌 함수를 반환
```jsx
const memoizedValue = useCallback(
    () => {
        doSomthing(의존성 변수1, 의존성 변수2);
    },
    [의존성 변수1, 의존성 변수2]
);
```
```jsx
// 두 코드는 동일한 역할을 함
useCallback(함수, 의존성 배열);

useMemo(() => 함수, 의존성 배열);
```

### useRef()
- Reference를 사용하기 위한 Hook
    - Reference: 특정 컴포넌트에 접근할 수 있는 객체
- refObject.`current`
    - current: 현재 참조하고 있는 Element
```jsx
const refContainger = useRef(초깃값);
```

## Hook의 규칙
### 1. Hook은 무조건 `최상위 레벨`에서만 호출해야 한다.
- 리액트 함수 컴포넌트의 최상위 레벨을 의미
    - 반복문, 조건문, 중첩된 함수들 안에서 Hook 호출 X
- Hook은 컴포넌트가 렌더링될 때마다 매번 같은 순서로 호출되어야 한다.

### 2. `리액트 함수 컴포넌트에서만` Hook을 호출해야 한다.

### [eslint-plugin-react-hooks](https://www.npmjs.com/package/eslint-plugin-react-hooks)

## Custom Hook 만들기
### Custom Hook을 만드는 상황
- 반복되는 로직이 반복될 때

### Custom Hook
- `이름이 use로 시작`하고 내부에서 다른 Hook을 호출하는 하나의 자바스크립트 함수
```jsx
// Custom Hook 추출
import React, { useState, useEffect } from "react";

function useUserStatus(userId) {
    const [isOnline, setIsOnline] = useState(null);

    useEffect(() => {
        function handleStatusChange(status) {
            setIsOnline(status.isOnline);
        }

        serverAPI.subscribeUserStatus(userId, handleStatusChange);
        return () => {
            ServerAPI.unsubscribeUserStatus(userId, handleStatusChange);
        };
    });

    return isOnline;
}
```
```jsx
// 사용
function UserStatus(props) {
    const isOnline = useUserStatus(props.user.id);

    if (isOnline === null) {
        return '대기중...';
    }
    return isOnline ? '온라인' : '오프라인';
}

function UserListItem(props) {
    const isOnline = useUserStatus(props.user.id);

    return (
        <li style={{colorL isOnline ? 'green' : 'black'}}>
            {props.user.name}
        </li>
    );
}
```

- 여러 개의 컴포넌트에서 하나의 Custom Hook을 사용할 때 컴포넌트 내부에 있는 모든 state와 effects는 전부 분리되어 있다.
- 각 Custom Hook 호출에 대해서 분리된 state를 얻게 됨
- 각 Custom Hook의 호출 또한 완전히 독립적이다.

### Hook들 사이에서 데이터를 공유하는 법
```jsx
const [userId, setUserId] = useState(1);
const isUserOnline = useUserStatus(userId);
// Hook 함수의 파라미터로 넣어서 데이터를 공유
```