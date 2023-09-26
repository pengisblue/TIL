# 9/26 강의
## 개요
### HTML 'form'
- 비정상적 혹은 악의적인 요청을 필터링할 수 없음
    - 유효한 데이터인지에 대한 확인이 필요
### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
#### 구현
- 유효성 검사를 구현하는 데에는 고려해야할 것이 많음
- Django가 제공하는 Form을 사용
## Django Form
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
    - 유효성 검사를 단순화 하고 자동화 할 수 있는 기능을 제공
### Form Class
### Widgets
- HTML 'input' element의 표현을 담당
## Django Model Form
### is_vaild()
- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환
## 참고
## Handling HTTP requests
