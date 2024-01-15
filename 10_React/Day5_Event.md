# day5 (1월 12일) 학습

## Event
### DOM의 Event
```javascript
<button onclick="activate()">
    Activate
</button>
```
### 리액트의 Event
- camel case
```jsx
<button onClick={activate}>
    Activate
</button>
```
- 예시
```jsx
// class Component
class Toggle extends React.Component {
  constructor(props) {
    super(props);

    this.state = { isToggleOn: true };

    // callback에서 `this`를 사용하기 위해서는 바인딩을 필수로 해줘야 한다.
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState((prevState) => ({
      isToggleOn: !prevState.isToggleOn,
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? "켜짐" : "꺼짐"}
      </button>
    );
  }
}
```
```jsx
// function Component
function Toggle(props) {
  const [isToggleOn, setIsToggleOn] = useState(true);

    // 방법1. 함수 안에 함수로 정의
  function handleClick() {
    setIsToggleOn((isToggleOn) => !isToggleOn);
  }

    // 방법2. arrow function을 사용하여 정의
  const handleClick = () => {
    setIsToggleOn((isToggleOn) => !isToggleOn);
  };

  return (
    <button onClick={handleClick}>
      {isToggleOn ? "켜짐" : "꺼짐"}
    </button>
  );
}
```

### 매개변수 전달
```jsx
// class Component
<button onClick={(event) => this.deleteItem(id, event)}>삭제</button>

<button onClick={this.deleteItem.bind(this, id)}>삭제</button>
```
```jsx
function MyButton(props) {
    const handleDelete = (id, event) => {
        console.log(id, event.target);
    };

    return (
        <button onClick={(event) => handleDelete(1, event)}>
            삭제
        </button>
    );
}
```