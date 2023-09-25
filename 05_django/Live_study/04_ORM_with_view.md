# 9/25 강의
## Read
### 전체 게시글 조회

### 단일 게시글 조회

## Create
#### Create 로직을 구현하기 위해 필요한 view 함수
- 사용자 입력 데이터를 받을 페이지
- 사용자가 입력한 데이터를 받아 DB에 저장

## HTTP request methods
> 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
- `GET` & `POST`
### `GET` Method
> R
- 특정 리소스를 `조회`하는 요청
    - (GET으로 데이터를 전달하면 Query String 형식으로 보내짐)
### `POST` Method
> C U D
- 특정 리소스에 `변경(생성, 수정, 삭제)을 요구하는` 요청
    - (POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐)
### 403 Forbidden
- 서버에 요청이 전달되었지만, `권한`때문에 거절됨
- CSRF token missing.
    - CSRF token이 누락되었음
### CSRF
> Cross-Site-Request-Forgery
- `사이트 간 요청 위조`
    - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여<br>
     특정 웹 페이지를 보안에 취약하게 하거나<br>
     수정, 삭제 등의 작업을 하게 만드는 공격 방법
####

## Delete
