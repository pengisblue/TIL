# 9/4 강의
## Web
> web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
### Web site
- `Web page`가 모인 것, 사용자들에게 정보나 서비스를 제공하는 공간
### Web page
- HTML, CSS 등의 웹 기술을 이용하여 만들어진, `Web site를 구성하는 하나의 요소`
- 구성요소
  - HTML: Structure
  - CSS: Styling
  - Javascript: Behavior

## 웹 구조화
### HTML
> Hyper Text Markup Language<br/>
> 웹 페이지의 의미와 구조를 정의하는 언어
#### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
#### Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- ex) HTML, Markdawn

### Structure of HTML
#### HTML Element(요소)
```html
<p>content</p>
```
- Element
    - Opening tag + content + Closing tag
#### HTML Attributes(속성)
```html
<p class="editor-note">content</p>
```
- 규칙
    - 요소 이름과 속성 사이에 공백이 있어야함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
    - 속성 값은 열고 닫는 따옴표로 감싸야 함
- 목적
    - 나타내고 싶진 않지만 `추가적인 기능, 내용`을 담고 싶을 때 사용
    - CSS에서 해당 `요소를 선택`하기 위한 값으로 활용됨
#### [01-html-basic](../01-fundamentals-of-html-css/01-html-basic.html)
### Text Structure
> HTML의 목적: `텍스트 구조와 의미`제공
```html
<h1>Heading</h1>
```
- 단순히 텍스트를 크게 만드는 것이 아닌 현재 `문서의 최상위 제목`이라는 의미 부여
#### [02-html-text-structure](../01-fundamentals-of-html-css/02-html-text-structure.html)
## 웹 스타일링
### CSS
> `Cascading` Style Sheet<br/>
> 웹페이지의 `디자인`과 `레이아웃`을 구성하는 언어
```css
/* 선택자 */
h1 {
    /* 선언 */
    /* 속성: 값 */
    color: red;
    font-size: 30px
}
```
#### CSS 적용 방법
1. 인라인 스타일: html 요소 안에 style 속성 값으로 작성 - 잘 사용 x
2. 내부 스타일 시트: head 태그 안에 style 태그 작성
3. 외부 스타일 시트: 별도 CSS 파일 생성 후 html 태그를 사용해 불러오기
#### CSS Selectors 종류
- 기본 선택자
  - 전체(*) 선택자
    - HTML 모든 요소를 선택
  - 요소(tag) 선택자
    - 지정한 모든 태그를 선택
  - 클래스(class) 선택자('.')
    - 주어진 클래스 속성을 가진 모든 요소를 선택
  - 아이디(id) 선택자('#')
    - 주어진 아이디 속성을 가진 요소 선택
    - 문서에서는 주어진 아이디를 가진 요소가 하나만 있어야 함
  - 속성(attr) 선택자 등
- 결합자 (Combinators)
  - 자식 결합자 (>)
  - 자손 결합자(" "(공백))
#### [03-css-selectors](../01-fundamentals-of-html-css/03-css-selectors.html)
#### Specificity (우선순위)
- Cascade(계단식)  
  - 동일한 우선순위를 갖는 규칙이 적용될 때, CSS에서 마지막에 나오는 규칙이 사용됨
```css
h1 {
    color: red;
}
h1 {
    color: purple;
}
/* purple이 적용 됨 */
```
#### [04-css-specificity](../01-fundamentals-of-html-css/04-css-specificity.html)
##### 우선순위 순서
1. Importance
    - !importance
        - `Cascade의 구조를 무시하고 강제로 스타일을 적용`하는 방식으로 권장X
2. Inline 스타일
3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 순서
### CSS 상속
- 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
#### 상속 여부
- 상속 되는 속성
  - Text 관련 요소 (font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
  - Box model 관련 요소 (width, height, border, box-sizing...)<br>
  position 관련 요소(position, top/right/bottom/left, z-index) 등
#### [05-css-inheritance](../01-fundamentals-of-html-css/05-css-inheritance.html)
#### [06-css-specificity_inheritance](../01-fundamentals-of-html-css/06-css-specificity_inheritance.html)
