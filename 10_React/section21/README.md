# 리액트 라우터가 있는 SPA 다중 페이지 구축하기

## React Router 설치

```bash
npm install react-router-dom
```

## 라우터 정의하기

```js
import { createBrowserRouter } from "react-router-dom";

import HomPage from "./pages/Home";

const router = createBrowserRouter([{ path: "/", element: <HomPage /> }]);
```

## 화면에 정의한 라우터를 보여주기

```js
import { createBrowserRouter, RouterProvider } from "react-router-dom";
// RouterProvider를 통해서 표시됨

function App() {
  return <RouterProvider router={router} />;
  //   RouterProvider는 router라는 프로퍼티를 가지고 있음
  //   createBrowserRouter가 생성한 페이지를 보여줌
}

export default App;
```

## Link

```jsx
import { Link } from "react-router-dom";
```

```jsx
<p>
  Go to <Link to="/products">the linst of products</Link>.
</p>
```

## 라우트 중첩

- 네비게이션바 만들기
- RouterProvider 주변의 컴포넌트는 렌더링 되지 않음
  - children 프로퍼티를 이용해서 라우트를 중첩해서 띄운다.

```js
const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      { path: "/", element: <HomPage /> },
      { path: "/products", element: <ProductsPage /> },
    ],
  },
]);
```

### 자식 라우터 렌더링하기

```js
import { Outlet } from "react-router-dom";
import MainNavigation from "../components/MAinNavigations";

export default function RootLayout() {
  return (
    <>
      <MainNavigation />
      <main>
        <Outlet />
        {/* 자식 라우터가 표시될 곳을 의미 */}
      </main>
    </>
  );
}
```

## NavLink
```js
import { NavLink } from "react-router-dom";
```
```js
// isActive를 통해서 현재 라우터와 링크가 일치하는지 확인할 수 있다.
// end는 path 중복을 방지하기위해 더이상 이어지는 링크가 없음을 표시
<NavLink
  to="/"
  className={({ isActive }) =>
    isActive ? classes.active : undefined
  }
  end
>
  Home
</NavLink>
```

## useNavigate
- Link를 이용하지 않고 라우터 이동시키기
```js
import { useNavigate } from "react-router-dom";

function HomPage() {
  const navigate = useNavigate();

  function navigateHandler() {
    navigate("/products");
  }

  return (
    <>
      <h1>Home</h1>
      <p>
        <button onClick={navigateHandler}>Navigate</button>
      </p>
    </>
  );
}

export default HomPage;

```