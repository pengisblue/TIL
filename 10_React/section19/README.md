# Redux (컨텍스트 API의 대안)

## 설치

```bash
npm install redux react-redux
```

## 소스파일 관리

- src/store/ 에서 관리

## 리액트용 리덕스 스토어 만들기

```js
// store/index.js

import { createStore } from "redux";

const counterReducer = (state = { counter: 0 }, action) => {
  if (action.type === "increment") {
    return {
      counter: state.counter + 1,
    };
  }

  if (action.type === "decrement") {
    return {
      counter: state.counter - 1,
    };
  }

  return state;
};

const store = createStore(counterReducer);

export default store;
```

## 스토어 제공하기

```js
import React from "react";
import ReactDOM from "react-dom/client";
// Provider를 import
import { Provider } from "react-redux";

import "./index.css";
import App from "./App";
// 작성한 store를 import
import store from "./store/index";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  // Provider의 store를 작성한 store로 설정
  <Provider store={store}>
    <App />
  </Provider>
);
```

## 컴포넌트에서 리덕스 데이터 사용하기

```js
// useSelector import
import { useSelector } from "react-redux";

import classes from "./Counter.module.css";

const Counter = () => {
  // 사용할 데이터를 선택해준다
  const counter = useSelector((state) => state.counter);

  const toggleCounterHandler = () => {};

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {/* 리덕스 데이터를 사용한다 */}
      <div className={classes.value}>{counter}</div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;
```

## 컴포넌트에서 Action을 Dispatch하기

```js
// useDispatch import
import { useSelector, useDispatch } from "react-redux";

import classes from "./Counter.module.css";

const Counter = () => {
  const dispatch = useDispatch();
  const counter = useSelector((state) => state.counter);

  // 사용할 action의 type을 dispatch한다
  const incrementHandler = () => {
    dispatch({ type: "increment" });
  };

  const decrementHandler = () => {
    dispatch({ type: "decrement" });
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      <div className={classes.value}>{counter}</div>
      <div>
        {/* 함수 적용 */}
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={decrementHandler}>Decrement</button>
      </div>
    </main>
  );
};

export default Counter;
```

## Action payload 추가하기

```js
// store/index.js
const counterReducer = (state = { counter: 0 }, action) => {
  if (action.type === "increase") {
    return {
      // action.amount를 통해 값을 동적으로 받는다
      counter: state.counter + action.amount,
    };
  }
};
```

```js
const increaseHandler = () => {
  // dispatch에 담아서 보내준다
  dispatch({ type: "increase", amount: 5 });
};
```

## State 속성 작업하기

```js
// 렌더링 여부를 결정할 showCounter를 추가
// 가독성을 위해 밖에서 정의
const initialState = { counter: 0, showCounter: true };

const counterReducer = (state = initialState, action) => {
  // ...

  if (action.type === "increase") {
    return {
      counter: state.counter + action.amount,
      // return하는 객체는 이전 값에 덮어쓰이기 때문에
      // 모든 action에서 다른 state도 가지고 있어야한다
      showCounter: state.showCounter,
    };
  }

  // ...

  // 새로운 action
  if (action.type === "toggle") {
    return {
      // 렌더링 여부를 토글
      showCounter: !state.showCounter,
      counter: state.counter,
    };
  }
};
```

```js
const Counter = () => {
  const dispatch = useDispatch();
  const counter = useSelector((state) => state.counter);
  // useSelector를 추가
  const show = useSelector((state) => state.showCounter);

  // dispatch 추가
  const toggleCounterHandler = () => {
    dispatch({ type: "toggle" });
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {/* show 여부에 따라 보인다 */}
      {show && <div className={classes.value}>{counter}</div>}
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};
```

## 리덕스에서 State를 사용할 때의 주의사항

- 절대 state를 `직접 변경하지 말것`
- 항상 `새로운 값`을 return해야 한다.

```js
// 잘못된 방식
if (action.type === "increment") {
  state.counter++; // 이렇게 state를 직접 변경하면 안된다

  return {
    counter: state.counter,
    showCounter: state.showCounter,
  };
}
```

## 리덕스 툴킷

```bash
npm install @reduxjs/toolkit
# 리덕스 툴킷에 리덕스가 포함되어있으므로 package.json에 리덕스가 있다면 삭제한다
```

## State 슬라이스 추가하기

```js
// createSlice를 import
import { createSlice } from "@reduxjs/toolkit";

const initialState = { counter: 0, showCounter: true };

createSlice({
  // Slice의 이름을 설정해줘야 한다
  name: "counter",
  // 초기 State설정 (initialState: initialState,)
  initialState,
  // 리듀서를 작성해준다
  reducers: {
    // action의 타입이 함수 이름이 됨 -> if문을 사용하지 않는다
    increment(state) {
      state.counter++; // 직접 state 값을 변경하는 것 처럼 보이지만 아님
    },
    decrement(state) {
      state.counter--;
    },
    // payload가 필요할 땐 action을 가져올 수 있다
    increase(state, action) {
      state.counter = state.counter + action.payload;
      // 툴킷이 payload로 보내줌
    },
    toggle(state) {
      state.showCounter = !state.showCounter;
    },
  },
});
```

## 리덕스 툴킷 연결

```js
// createStore 대신 configureStore를 사용한다
import { createSlice, configureStore } from "@reduxjs/toolkit";

const initialState = { counter: 0, showCounter: true };

const counterSlice = createSlice({
  //   ...
});

// 리듀서를 하나로 합쳐줌
const store = configureStore({
  reducer: counterSlice.reducer,
  // 프로젝트가 커질 경우 아래처럼 리듀서를 매핑
  // reducer: { counter: counterSlice.reducer },
});

export default store;
```

## 리덕스 툴킷으로 마이그레이션하기

```js
// store/index.js에서 counterActions를 export
export const counterActions = counterSlice.actions;
```

```js
// 사용하려는 컴포넌트에서 import
import { counterActions } from "../store/index";

// 이렇게 쓸 수 있다
const incrementHandler = () => {
  dispatch(counterActions.increment());
};

// payload가 있을 경우
const increaseHandler = () => {
  dispatch(counterActions.increase(10)); // { type: SOME_UNIQUE_IDENTIFIER (= increase), payload: 10 } 형태
};
```

## 다중 슬라이스 작업

```js
// store/index.js
import { createSlice, configureStore } from "@reduxjs/toolkit";

// 새로운 state 정의
const initialAuthState = {
  isAuthenticated: false,
};

// 새로운 slice 생성
const authSlice = createSlice({
  name: "authentication",
  initialState: initialAuthState,
  reducers: {
    login(state) {
      state.isAuthenticated = true;
    },
    logout(state) {
      state.isAuthenticated = false;
    },
  },
});

// 리듀서를 객체로 묶어준다
const store = configureStore({
  reducer: { counter: counterSlice.reducer, auth: authSlice.reducer },
});

export const counterActions = counterSlice.actions;
// 액션도 export
export const authActions = authSlice.actions;

export default store;
```

```js
// reducer의 형식이 바꼈으므로
// Counter.js의 selector를 변경해준다
const counter = useSelector((state) => state.counter.counter);
const show = useSelector((state) => state.counter.showCounter);
```

## 로그인 로그아웃 상태 변경

```js
// App.js
import { Fragment } from "react";
import { useSelector } from "react-redux";

import Counter from "./components/Counter";
import Header from "./components/Header";
import Auth from "./components/Auth";
import UserProfile from "./components/UserProfile";

function App() {
  // useSelector로 auth 리듀서의 state 가져오기
  const isAuth = useSelector((state) => state.auth.isAuthenticated);

  return (
    <Fragment>
      <Header />
      {/* 로그인 안했을 때 */}
      {!isAuth && <Auth />}
      {/* 로그인 했을 때 */}
      {isAuth && <UserProfile />}
      <Counter />
    </Fragment>
  );
}

export default App;
```

```js
// 로그인 상태로 변경하기
// components/Auth.js
import { useDispatch } from "react-redux";

import classes from "./Auth.module.css";
import { authActions } from "../store/index";

const Auth = () => {
  const dispatch = useDispatch();

  // 로그인 핸들러에서
  const loginHandler = (event) => {
    event.preventDefault();
    // 로그인 action
    dispatch(authActions.login());
  };
};

export default Auth;
```

```js
// 헤더에 렌더링 되는 내용 설정, 로그아웃
// components/Header.js
import { useDispatch, useSelector } from "react-redux";

import classes from "./Header.module.css";
import { authActions } from "../store/index";

const Header = () => {
  const dispatch = useDispatch();

  // useSelector로 auth 리듀서의 state 가져오기
  const isAuth = useSelector((state) => state.auth.isAuthenticated);

  // 로그아웃 action
  const logoutHandler = () => {
    dispatch(authActions.logout());
  };

  return (
    <header className={classes.header}>
      <h1>Redux Auth</h1>
      {/* 로그인 상태에서만 보인다 */}
      {isAuth && (
        <nav>
          <button onClick={logoutHandler}>Logout</button>
        </nav>
      )}
    </header>
  );
};

export default Header;
```

## 코드 분할하기
- store에 slice별로 분할 후 컴포넌트의 import위치 수정
```js
// store/auth.js
// auth리듀서 분할
// counterSlice도 같은 방법으로 분할한다
import { createSlice } from "@reduxjs/toolkit";

const initialAuthState = {
  isAuthenticated: false,
};

const authSlice = createSlice({
  name: "authentication",
  initialState: initialAuthState,
  reducers: {
    login(state) {
      state.isAuthenticated = true;
    },
    logout(state) {
      state.isAuthenticated = false;
    },
  },
});

export const authActions = authSlice.actions;

// 리듀서를 export
export default authSlice.reducer;
```

```js
// sotre/index.js
// 분할이 완료된 index.js
import { configureStore } from "@reduxjs/toolkit";

import counterReducer from "./counter";
import authReducer from "./auth";

const store = configureStore({
  reducer: { counter: counterReducer, auth: authReducer },
});

export default store;
```
