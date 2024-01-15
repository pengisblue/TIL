# day2 (1월 9일) 학습

## 리액트의 장점과 단점
### 장점
- 렌더링 속도
    - Virtual DOM을 사용하여 빠른 렌더링 속도를 가짐
- 재사용성
    - 컴포넌트 기반의 구조를 가져서 재사용성이 높음
- 넓은 커뮤니티

### 단점
- 학습 곡선
- 높은 상태관리 복잡도
    - -> 외부 상태관리 라이브러리로 극복

## JSX
> A syntax extension to JavaScript (JavaScript + XML/HTML)

### JSX의 장점
- 코드의 간결함, 가독성 향상
- Injection Attacks 방어

### 사용
```jsx
function getGreeting(user) {
    if (user) {
        return <h1>Hello, {formatName(user)}!</h1>;
    }
    return <h1>Hello, Stranger.</h1>;
}
```

### [실습](./frontend/src/chap_03/)

## Elements
- 리액트 Elements는 자바스크립트 객체 형태로 존재

### 구성
```jsx
React.createElement(
    type,
    [props],
    [...children]
)
```

### 특징
- immutable
    - Elements 생성 후에는 children이나 attributes를 바꿀 수 없다.

### [실습](./frontend/src/chap_04/)

## Components와 Props
> props -> React components -> React element

### Props (property)
- 컴포넌트에 전달할 다양한 정보를 담고있는 자바스크립트 객체
- 특징
    - Read-only : 모든 리액트 컴포넌트는 Props를 직접 바꿀 수 없고, 같은 Props에 대해서는 항상 같은 결과를 보여줄 것
- 사용법
```jsx
function App(props) {
    return (
        <Layout
            width={2560}
            height={1440}
            header={
                <Header title="블로그"/>
            }
            footer={
                <Footer />
            }
        />
    );
}
```