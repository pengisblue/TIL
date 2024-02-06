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
  className={({ isActive }) => (isActive ? classes.active : undefined)}
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

## 동적 라우트

```js
// ':'뒤에 변수명을 적어준다
{ path: "/products/:productId", element: <ProductDetailPage /> },
```

```js
// 할당은 `${}`에 변수를 넣어줄 수 있다
<li key={product.id}>
  <Link to={`/products/${product.id}`}>{product.title}</Link>
</li>
```

### params 사용

```js
import { useParams } from "react-router-dom";

export default function ProductDetailPage() {
  const params = useParams();

  return (
    <>
      <h1>Product Details</h1>
      <p>{params.productId}</p>
    </>
  );
}
```

## 상대경로와 절대경로

```js
// 절대 경로
{
  path: "/",
  element: <RootLayout />,
  children: [
    { path: "/", element: <HomPage /> },
    { path: "/products", element: <ProductsPage /> },
    { path: "/products/:productId", element: <ProductDetailPage /> },
  ],
},
```

```js
// 상대 경로
// 맨 앞의 '/'가 절대 경로를 의미한다
{
  path: "/",
  element: <RootLayout />,
  children: [
    { path: "", element: <HomPage /> },
    { path: "products", element: <ProductsPage /> },
    { path: "products/:productId", element: <ProductDetailPage /> },
  ],
},
```

### Link 상대경로

```js
<li key={product.id}>
  <Link to={product.id}>{product.title}</Link>
  {/* 상대경로로 작성되어 '/products/:productID'로 이동한다 */}
</li>
```

### 상위 경로로 이동

```js
// '..'은 상위 경로로 이동한다는 의미

<Link to={'..'} relative="router">back</Link>
// router에 정의된 부모 경로로 이동한다
// '/'로 이동

<Link to={'..'} relative="path">back</Link>
// 이전 경로로 이동한다
// '/products/:productsId'에서 '/products'로 한 단계 상위 이동
```

## index 라우트

```js
// '/'빈 경로일 경우에 index로 표시할 수도 있다.
{ index: true, element: <HomPage /> },
```
