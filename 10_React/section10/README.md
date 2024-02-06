# 리액트의 컨텍스트 API & userReducer - 상태 관리 심화

## 컨텍스트 API

- 리액트의 상태를 컨텍스트 값에 연결하여 모든 컴포넌트에서 사용할 수 있게 한다.

## 컨텍스트 만들기

- 관습적으로 store폴더에 만든다

```jsx
// src/store/shopping-cart-context.jsx
import { createContext } from "react";

// 리액트 컴포넌트가 들어가있을 컨텍스트
export const CartContext = createContext({
  items: [],
});
```

## 컴포넌트에 부여하기

- 컨텍스트를 사용할 곳을 감싸준다
- Provider는 직접 작성한 것이 아닌 리액트에 있는 컴포넌트

```jsx
// App.js
<CartContext.Provider value={{ items: [] }}>
  <Header
    cart={shoppingCart}
    onUpdateCartItemQuantity={handleUpdateCartItemQuantity}
  />
  <Shop onAddItemToCart={handleAddItemToCart}>
    {DUMMY_PRODUCTS.map((product) => (
      <li key={product.id}>
        <Product {...product} onAddToCart={handleUpdateCartItemQuantity} />
      </li>
    ))}
  </Shop>
</CartContext.Provider>
```

## 컨텍스트 사용하기

```jsx
// 사용 전
export default function Cart({ items, onUpdateItemQuantity }) {
  const totalPrice = items.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );
}
```

```jsx
// 사용 후
import { useContext } from "react";

import { CartContext } from "../store/shopping-cart-context";

export default function Cart({ onUpdateItemQuantity }) {
  const { items } = useContext(CartContext);
  // useContext훅을 사용해서 컨텍스트 사용

  const totalPrice = items.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );
}
```

## State와 연결

```jsx
const ctxValue = {
  items: shoppingCart.items,
  addItemToCart: handleAddItemToCart, // 함수를 value값에 사용
};

return (
  <CartContext.Provider value={ctxValue}>
    <Header
      cart={shoppingCart}
      onUpdateCartItemQuantity={handleUpdateCartItemQuantity}
    />
    <Shop onAddItemToCart={handleAddItemToCart}>
      {DUMMY_PRODUCTS.map((product) => (
        <li key={product.id}>
          <Product {...product} />
          {/* 함수를 props로 전달하지 않아도 사용할 수 있게 된다 */}
        </li>
      ))}
    </Shop>
  </CartContext.Provider>
);
```

```jsx
// Product
import { useContext } from "react";

import { CartContext } from "../store/shopping-cart-context";

export default function Product({ id, image, title, price, description }) {
  const { addItemToCart } = useContext(CartContext);

  return (
    <article className="product">
      <img src={image} alt={title} />
      <div className="product-content">
        <div>
          <h3>{title}</h3>
          <p className="product-price">${price}</p>
          <p>{description}</p>
        </div>
        <p className="product-actions">
          <button onClick={() => addItemToCart(id)}>Add to Cart</button>
        </p>
      </div>
    </article>
  );
}
```

## 컨텍스트 아웃소싱

- App.js에 있던 컨텍스트로 사용할 함수 로직을 외부로 빼내준다

```jsx
// store/shopping-cart-context.jsx
import { createContext, useState } from "react";

import { DUMMY_PRODUCTS } from "../dummy-products.js";

// 리액트 컴포넌트가 들어가있을 컨텍스트
export const CartContext = createContext({
  items: [],
  addItemToCart: () => {},
  updateItemQuantity: () => {},
});

// 여기가 원래 App.js에 있던 로직 부분
export default function CartContextProvider({ children }) {
  const [shoppingCart, setShoppingCart] = useState({
    items: [],
  });

  function handleAddItemToCart(id) {
    setShoppingCart((prevShoppingCart) => {
      const updatedItems = [...prevShoppingCart.items];

      const existingCartItemIndex = updatedItems.findIndex(
        (cartItem) => cartItem.id === id
      );
      const existingCartItem = updatedItems[existingCartItemIndex];

      if (existingCartItem) {
        const updatedItem = {
          ...existingCartItem,
          quantity: existingCartItem.quantity + 1,
        };
        updatedItems[existingCartItemIndex] = updatedItem;
      } else {
        const product = DUMMY_PRODUCTS.find((product) => product.id === id);
        updatedItems.push({
          id: id,
          name: product.title,
          price: product.price,
          quantity: 1,
        });
      }

      return {
        items: updatedItems,
      };
    });
  }

  function handleUpdateCartItemQuantity(productId, amount) {
    setShoppingCart((prevShoppingCart) => {
      const updatedItems = [...prevShoppingCart.items];
      const updatedItemIndex = updatedItems.findIndex(
        (item) => item.id === productId
      );

      const updatedItem = {
        ...updatedItems[updatedItemIndex],
      };

      updatedItem.quantity += amount;

      if (updatedItem.quantity <= 0) {
        updatedItems.splice(updatedItemIndex, 1);
      } else {
        updatedItems[updatedItemIndex] = updatedItem;
      }

      return {
        items: updatedItems,
      };
    });
  }

  const ctxValue = {
    items: shoppingCart.items,
    addItemToCart: handleAddItemToCart,
    updateItemQuantity: handleUpdateCartItemQuantity,
  };

  // 여기서 리턴해주면서 컨텍스트를 사용할 컴포넌트는 children이 된다
  return (
    <CartContext.Provider value={ctxValue}>{children}</CartContext.Provider>
  );
}
```

```jsx
// 가벼워진 App.js 코드
import Header from "./components/Header.jsx";
import Shop from "./components/Shop.jsx";
import Product from "./components/Product.jsx";
import { DUMMY_PRODUCTS } from "./dummy-products.js";
import CartContextProvider from "./store/shopping-cart-context.jsx";

function App() {
  return (
    // 위에서 리턴한 부분
    <CartContextProvider>
      <Header />
      <Shop onAddItemToCart={handleAddItemToCart}>
        {DUMMY_PRODUCTS.map((product) => (
          <li key={product.id}>
            <Product {...product} />
          </li>
        ))}
      </Shop>
    </CartContextProvider>
  );
}

export default App;
```

## useReducer

```jsx
const [state, dispatch] = useReducer();
// dispatch로 보낸 액션이 리듀서 기능에 의해 사용된다
```
