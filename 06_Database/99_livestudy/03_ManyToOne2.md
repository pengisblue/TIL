# 10/12 강의
## Article(N) & User(1)
### 모델 관계 설정
#### User 모델을 참조하는 2가지 방법
> django 프로젝트의 '내부 구동 순서'와 '반환 값'에 따른 이유
1. get_user_model()
    - 반환값: User Object(객체)
    - 사용위치: models.py가 아닌 모든 위치
2. setting.AUTH_USER_MODEL
    - accounts.User(문자열)
    - 사용위치: models.py

### 게시글 CREATE

### 게시글 UPDATE

### 게시글 DELETE

## User & Comment

## 참고