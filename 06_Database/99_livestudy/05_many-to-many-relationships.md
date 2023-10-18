# 10/17 강의
## 팔로우
### 프로필 구현
```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('profile/<str:username>/', views.profile, name='profile'),
]

```

### 팔로우 기능 구현
#### User(M) - User(N)
> 0명 이상의 회원은 0명 이상의 회원과 관련
- ManyToManyField 작성
```python

```

## 참고
### exists
```python

```

## Fixtures
- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
    - 데이터베이스 구조에 맞추어 작성 되어있음
- 초기 데이터 제공

### Fixtures 활용
#### 사전 준비
- M:N 까지 모두 작성된 Django 프로젝트에서 유저, 게시글, 댓글 등 각 데이터를 최소 2~3개 이상 생성해두기

#### 관련 명령어
- dumpdata
    - 생성(데이터 추출)
    - json 형식으로 저장
```bash
$ python manage.py dumpdata appname.modelname > filename.json
```
- loaddata
    - 로드(데이터 입력)
    - Fixtures 기본 경로
        - app_name/fixtures/
```bash
$ python manage.py loaddata {경로}
```

## 쿼리 개선
- 같은 결과를 얻기 위해 DB측에 보내는 쿼리 개수를 점차 줄여 조회하기

### annotate
- SQL의 GROUP BY 쿼리를 사용

### select_related
- SQL의 INNER JOIN 쿼리를 활용
    - 1:1또는 N:1 참조 관계에서 사용

### prefetch_related
- M:N 또는 N:1 역참조 관계에서 사용
    - SQL이 아닌 Python 을 사용한 JOIN을 진행

### select_related & prefetch_related