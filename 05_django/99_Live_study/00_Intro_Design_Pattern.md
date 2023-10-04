# 9/12 강의
## Framework
### Django framework
> Python 기반의 대표적인 웹 프레임워크
### 클라이언트와 서버
#### Client
- 서비스를 `요청`하는 주체 (웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)
#### Server
- 클라이언트의 요청에 `응답`하는 주체 (웹 페이지, 앱을 저장하는 컴퓨터)
### 프로젝트 및 가상환경
#### 가상환경
> Python 애플리케이션과 그에 따른 패키지들을 `격리`하여 관리할 수 있는 `독립적인` 개발 환경
- 가상환경 생성
```bash
$ python -m venv {가상환경이름}
```
- 가상환경 활성화
```bash
$ source venv/Scripts/activate
```
- 비활성화
```bash
$ deactivate
```
- 환경에 설치된 패키지 목록 확인
```bash
$ pip list
```
- 의존성 패키지 목록 생성
```bash
$ pip freeze > requirements.txt
```
- requirements.txt 의 pip 한번에 받기
```bash
$ pip install -r requirements.txt
```
#### Django 프로젝트 생성 전 루틴
```bash
# 1. 가상환경(venv) 생성
$ python -m venv venv

# 2. 가상환경 활성화
$ source venv/Scripts/activate

# 3. Django 설치
$ pip install Django

# 4. 의존성 파일 생성
$ pip freeze > requirements.txt
```
#### Django 프로젝트 생성
```bash
# $ django-admin startproject {프로젝트이름} {디렉토리 위치}
$ django-admin startproject firstpjt .
```
#### Django 서버 실행
```bash
$ python manage.py runserver
```
## Django Design Pattern
### Django 프로젝트와 앱
- Django project
    - 애플리케이션의 집합
    - DB설정, URL 연결, 전체 앱 설정 등을 처리
- Django application
    - 독립적으로 작동하는 기능 단위 모듈
    - 각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성
#### 앱 사용 과정
- 앱 생성
```bash
# $ python manage.py startapp {앱이름}
$ python manage.py startapp articles
```
- 앱 등록
    - 프로젝트 파일 > setting.py > INSTALLED_APPS에 앱 이름 추가

- `앱 등록 후 생성은 불가능`

### Django 디자인 패턴
#### MVC 디자인 패턴
> Model(DB), View(화면), Controller(내부 로직)
- 애플리케이션을 구조화하는 대표적인 디자인 패턴
    - 시각적 요소와 뒤에서 실행되는 로직을 `독립적이고 쉽게 유지 보수`할 수 있는 애플리케이션을 만들기 위하여
#### MTV 디자인 패턴
> Model, Template, View
- Django에서 애플리케이션을 구조화하는 패턴
    - 기존 MVC패턴과 동일하나 명칭을 다르게 정의한 것
- View -> Template
- Controller -> View
#### 프로젝트 구조
- `settings.py`
- `urls.py`
- __init__.py
- asgi.py
- wsgi.py
- manage.py
#### 앱 구조
- admin.py
- models.py
- views.py
    - contraller
- apps.py
- tests.py
### 요청과 응답
- 요청 -> urls.py -> app(views.py) -> 응답
