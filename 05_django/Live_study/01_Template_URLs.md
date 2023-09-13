# 9/13 강의
## Django Template & URLs
### Django Template Language (DTL)
> Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
1. Variable
    - render함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot(.)을 사용하여 변수 속성에 접근할 수 있음
    ```html
    {{ variable}}
    ```
2. Filters
    - 표시할 변수를 수정할 때 사용
    - chained가 가능하며 일부 필터는 인자를 받기도 함    
    ```html
    {{ variable|filter }}
    {{ name|truncatewords:30 }}  <!-- 문자를 자르는 필터 -->
    ```
3. Tags
    - 반복 or 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    ```html
    {% tag %}
    {% if %} {% endif %}
    ```
4. Comments(주석)
    ```html
    {# name #}
    {% comment %}
        {% if name == 'Sophia' %}
        {% endif %}
    {% endcomment %}
   ```
### 템플릿 상속
- `페이지의 공통요소를 포함`하고 `하위 템플릿이 재정의 할 수 있는 공간`을 정의하는<br/>
기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
- 'extends' tag
    - `템플릿 최상단에 작성` (2개 이상 사용 불가)
    ```django
    {% extends 'path' %}
    ```
- 'block' tag
    - 하위 템플릿에서 재정의 할 수 있는 블록을 정의
    ```django
    {% block name %}{% enblock name %}
    ```
## HTML form (요청과 응답)
### 데이터를 보내고 가져오기
- HTML form은 HTTP요청을 서버에 보내는 가장 편리한 방법
### 'form' element
- 사용자로부터 할당된 데이터를 서버로 전송
> 웹에서 사용자 정보를 입력하는 여러 방식을 제공 (text, password, checkbox 등)
#### 속성
- action
    - 데이터를 어디로 보내는가
- method
    - 어떤 방식으로 보내는가
- input
    - 사용자의 데이터를 입력 받을 수 있는 요소 (type속성에 따라 데이터를 받음)
- name
    - 입력한 데이터에 붙이는 이름(key)
    > 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근
#### Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 보내는 방법
- key=value 쌍으로 구성
#### HTTP request 객체
> form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨있음

## Django URLs
### Variable routing 작성법
#### Path converter

