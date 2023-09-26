# 9/14 강의
## Django Model
### Model
> DB 테이블을 `정의`하고 데이터를 `조작`할 수 있는 기능들을 제공(테이블 구조를 설계하는 청사진)
#### model 클래스 작성
```python
# articles/models.py

class Article(models.Model):    # models모듈.Model클래스 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
```
- 작성한 모델 클래스는 최종적으로 DB에 테이블 구조를 만듦<br>
`모델 클래스 == 테이블 설계도`

    |id|title|content|
    |:--:|:--:|:--:|
    |..|..|..|
    |..|..|..|

#### model 클래스
- django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
- Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스
> 개발자는 `테이블 구조를 어떻게 설계할지에 대한 코드`만 작성하도록 하기 위한 것
- 클래스 변수명
    - 테이블의 각 `필드(열) 이름`
    > 행: 레코드, 열: 필드
- model Field 클래스
    - 테이블 필드의 `데이터 타입을 의미`
    - 키워드 인자: 테이블 필드의 `제약조건` 관련 설정
    > 제약조건: 숫자만 저장되도록, 문자가 100자 까지만 저장되도록 등
## Migrations
- model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법
### 명령어
```bash
# model class를 기반으로 최종 설계도(migration) 작성
$ python manage.py makemigrations
```
```bash
# 최종 설계도를 DB에 전달하여 반영
$ python manage.py migrate
```
### 추가 Migrations
> 이미 생성된 테이블에 필드를 추가하기
#### 추가 모델 필드 작성
1. model class 변경
```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
2. default 값이 없기 때문에 makemigrations가 불가능 하다
```bash
$ python manage.py makemigrations
It is impossible to add the field 'created_at' with 'auto_now_add=True' to article without providing a default. This is because the database needs something to populate existing rows.
# 현재 대화를 유지하면서 직접 디폴트 값을 입력하는 방법  
 1) Provide a one-off default now which will be set on all existing rows
# 현재 대화를 나간 후 models.py에 기본 값 관련 설정을 하는 방법
 2) Quit and manually define a default value in models.py.
Select an option:
```
3. Select 1
```bash
Select an option: 1
# 날짜 데이터이기 때문에 Django가 제안하는 디폴트값을 사용
Please enter the default value as valid Python.
Accept the default 'timezone.now' by pressing 'Enter' or provide another value.       
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
# 입력 없이 enter를 누르면 Django가 제안하는 디폴드 값으로 설정 됨
[default: timezone.now] >>>
```
4. migrations 과정 종료 후 2번째 migration 파일이 생성 됨
```bash
Migrations for 'articles':
  articles\migrations\0002_article_created_at_article_updated_at.py
    - Add field created_at to article
    - Add field updated_at to article
```
5. migrate 후 테이블 필드 변화 확인
```bash
$ python manage.py migrate
```
### Model Field
> DB 테이블의 필드(열)를 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의
#### CharField()
- 길이의 제한이 있는 문자열을 넣을 때 사용
    - 필드의 최대 길이를 결정하는 `max_length`는 필수 인자
#### TextField()
- 글자 수가 많을 때 사용
#### DateTimeField()
- 날짜와 시간을 넣을 때 사용
- 선택인자
    - auto_now<br>
        : 데이터가 `저장될 때 마다` 자동으로 현재 날짜시간을 저장
    - auto_now_add<br>
        : 데이터가 `처음 생성될 때만` 자동으로 현재 날짜시간을 저장
## Admin site
### Automatic admin interface
- 자동으로 관리자 인터페이스를 제공
#### admin 계정 생성
```bash
$ python manage.py createsuperuser
```
```bash
Username (leave blank to use 'ssafy'): admin    # id
Email address: admin@ssafy.com  # email (선택사항)
Password:   # 보안상 터미널에 직접 출력되지 않음
Password (again):
# 비밀번호가 간단해서 발생한 안내
The password is too similar to the username.
This password is too common.
# 무시하고 생성하기 : y
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

# sql의 auth_user에서 확인 가능
```
#### admin에 모델 클래스 등록
> admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
```python
# articles/admin.py

from django.contrib import admin
# 명시적 상대경로
from .models import Article     # 등록하기위해 import

# Article 모델 클래스를  admin site에 등록
# admin site에 등록(register)한다
admin.site.register(Article)
```
## 참고
### 데이터베이스 초기화
1. migration 파일 삭제
2. db.sqlite3 파일 삭제
- 삭제하면 안되는 파일과 폴더
    - `migrations 폴더`
    - `__init__.py 파일`
### Migrations 기타 명령어
```bash
$ python manage.py showmigrations
# migrations 파일들이 migrate 됐는지 안됐는지 확인하는 명령어
# [X] 표시가 있으면 migrate가 완료되었음을 의미
```
```bash
$ python manage.py sqlmigrate articles 0001
# 해당 migrations 파일이 SQL 언어로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어
```
### 첫 migrate시 출력이 많은 이유?
- Django 프로젝트가 동작하기위해 미리 작성 되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate되기 때문
### SQLite
- Django의 기본 데이터베이스
### CRUD
> 소프트웨어가 가지는 기본적인 데이터 처리 기능
- Create
- Read
- Update
- Delete