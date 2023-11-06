# 10/12 강의
## Computed Properties
### Computed
- 계산된 속성을 정의하는 함수
    - 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

#### 특징
- 반환된 값은 computed ref
- computed 속성은 의존된 반응형 데이터를 `자동으로 추적`
- 의존하는 데이터가 변경될 때만 재평가

### Computed vs Methods

#### computed와 method 차이
- computed
    - `의존된 반응형 데이터를 기반으로 캐시(cached)된다.`
    - 의존하는 데이터가 변경된 경우에만 재평가됨
- method
    - 렌더링이 발생할 때마다 항상 함수를 실행

#### Cache (캐시)
- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근

#### 적절한 사용처
- computed
- method

## Conditional Rendering
### v-if
- 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링

### v-show
- 표현식 값의 T/F를 기반으로 요소의 가시성을 전환

### v-if vs v-show
- v-if (Cheap initial load, expensive toggle)
    - 초기 조건이 false인 경우 아무 작업도 수행하지 않음
    - 토글 비용이 높음

- v-show (Expensive initial load, cheap toggle)
    - 초기 조건에 관계없이 항상 렌더링
    - 초기 렌더링 비용이 더 높음

## List Rendering
### v-for
- 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링 
- `alias in expression` 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(alias)을 제공
```html
<div v-for="item in items">
  {{ item.text }}
</div>
```

### v-for with key
- **`반드시 v-for와 key를 함께 사용한다`**
    - 내부 컨포넌트의 상태를 일관되게 유지

### v-for with v-if

## Watchers
- watch()

### watch 구조
- variable
    - 감시하는 변수
- newValue
    - 감시하는 변수가 변화된 값
- oldValue
    - 감시하는 변수의 변화 전 값

## Lifecycle Hooks

## Vue Style Guide