# 메뉴 관리 시스템
> ModelForm을 사용하여 레스토랑의 메뉴 관리 시스템을 만들고자 한다. 요구 사항을 만족하는 프로젝트를 구성하시오.


### CR 기능 구현
- 요구 사항
1. gitignore를 포함하여야 한다.
2. 새로운 가상 환경을 생성하고, 가상 환경 내에서 django를 설치한다.
3. project 명은 menu_management로 생성한다.
4. app 명은 menus로 생성한다.
5. Menu model을 정의한다.
    - 정의해야 할 필드 정보는 첨부 파일을 참고
6. '/menus/' 경로로 요청시 전체 메뉴 목록을 확인 할 수 있어야 한다.
    - 메뉴 생성 페이지로 이동할 수 있는 링크를 제공한다.
    - 각 메뉴의 상세 정보 페이지로 이동할 수 있는 링크를 제공한다.
7. '/menus/new/' 경로로 요청시 게시글 생성을 위한 form을 보여준다.
    - form은 데이터를 POST 방식으로 전송한다.
    - 작성한 데이터는 '/menus/create/' 경로로 전송한다.
8. '/menus/create/' 경로에서는 데이터를 저장하고 '/menus/{menu_pk}/' 경로로 redirect 한다.
9. '/menus/{menu_pk}/' 경로로 요청시 메뉴 상세 목록을 확인할 수 있는 페이지를 제공한다.
10. base template을 사용하여 template을 상속받아야 한다.
11. 메뉴 생성을 위한 html form은 django의 ModelForm을 사용하여 구현한다.


### UD 기능 구현
- 요구 사항
1. '/menus/{menu_pk}/edit/' 경로로 요청시 메뉴 정보 수정을 위한 form을 보여준다.
    - form은 데이터를 POST 방식으로 전송한다.
    - form은 기존 메뉴 정보를 포함하고 있어야 한다.
    - 작성한 데이터는 '/menus/{menu_pk}/update/' 경로로 전송한다.
2. '/menus/{menu_pk}/update/' 경로에서는 데이터를 수정하고 '/menu/{menu_pk}/' 경로로 redirect 한다.
3. '/menus/{menu_pk}/delete/' 경로로 요청시 메뉴가 삭제되어야 한다.
4. base template을 사용하여 template을 상속받아야 한다.


### 코드 개선
- 요구 사항
1. '/menus/' 경로에서 메뉴 정보를 가격순으로 내림차순 정렬하여 보여준다.
. '/menus/new/' 경로와 '/menus/create/' 경로를 하나로 통합하고, 클라이언트의 요청 방식에 따라 적절한 로직이 실행되도록 조건분기를 구분하시오.
3. '/menus/{menu_pk}/edit/' 경로와 '/menus/{menu_pk}/update/' 경로를 하나로 통합하고, 클라이언트의 요청 방식에 따라 적절한 로직이 실행되도록 조건분기를 구분하시오.
4. '/menus/{menu_pk}/delete/' 경로로 요청시 게시글이 삭제되어야 한다.
    - 단, 반드시 POST 요청일 때만 게시글이 삭제되도록 한다.
5. 메뉴 상세 페이지에서 비건 여부에 따라 나타내는 글자를 다음과 같이 변경한다.
    - 비건 여부가 True인 경우, '채식 위주의 식단 구성!'
    - 비건 여부가 False인 경우, '고기를 포함한 식단 구성!'
6. 관리자 페이지에서 메뉴들을 관리 할 수 있어야 한다.
    - 관리자 페이지에서는 메뉴 목록에는 메뉴의 이름이 목록에 표기되도록 한다.


### widget 활용하기
- 요구 사항
1. bootstrap CDN을 base template에 작성한다.
2. ModelForm widget을 활용하여 bootstrap form 관련 class를 부여한다.
    - label은 무시한다.
    - 각 input 혹은 textarea에 대해서만 class를 부여한다.
3. name field에 placeholder를 추가한다.
    - 메뉴 이름을 작성해 주세요. 문구를 표기한다.
4. description field에 placeholder를 추가한다.
    - 메뉴 설명을 작성해 주세요. 문구를 표기한다.
5. create & update 버튼을 적절한 색상의 button tag로 변경한다.