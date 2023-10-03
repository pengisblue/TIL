# 9/27 강의
## Static files(정적 파일)
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)
- `정적 파일을 제공하기 위한 경로(URL)`가 있어야 함

### Static files 제공하기
> Templates와 같은 원리라고 생각하면 됨
- Static files 기본 경로
    - app폴더/static/

#### STATIC_URL
- 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
- 실제 파일이나 디렉토리가 아니며, URL로만 존재
```python
# setting.py

STATIC_URL = 'static/'
```
- URL + STATIC_URL + 정적파일 경로
> http://127.0.0.1:8000/static/articles/sample-1.png

#### 1. 기본 경로에서 제공하기
- static을 적용할 html파일에 static load해오기(import)
```html
<!-- articels/index.html -->
<!-- 이 이후로 static이 적용 -->
{% load static %}
```
##### 이미지 가져오기
- articles/static/articles/ 경로에 이미지 파일 배치
- static tag를 사용해 이미지 파일에 대한 url 제공

```html
<!-- articels/index.html -->

<body>
  <!-- static 태그로 url 작성 -->
  <img src="{% static "articles/sample-1.png" %}" alt="샘플이미지">
</body>
```

##### css 가져오기
- articles/static/articles/ 경로에 css 파일 배치
```css
/* articles/style.css */

h1 {
  color: red;
}
```

- static tag를 사용해 css 파일에 대한 url 제공
```html
<!-- articles/index.html -->

<head>
    <link rel="stylesheet" href="{% static "articles/style.css" %}">
</head>
```

#### 2. 추가 경로에서 제공하기
- STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
    - 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
```python
# setting.py

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
- 추가 경로에 이미지 파일 배치
- static tag를 사용해 이미지 파일에 대한 url 제공
```html
<!-- articels/index.html -->

<body>
  <!-- static 태그로 url 작성 -->
  <img src="{% static "sample-2.png" %}" alt="sample2">
</body>
```
### 정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요

## Media files
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

### 이미지 업로드
#### ImageField()
- 이미지 업로드에 사용하는 모델 필드
- `이미지 파일의 경로`가 문자열로 DB에 저장
    - 이미지 객체 직접 저장 X

#### 사전 준비
- setting.py에 MEDIA_ROOT, MEDIA_URL 설정
- 작성한 MEDIA_ROOT, MEDIA_URL에 대한 url 지정
- MEDIA_ROOT
    - 미디어 파일들이 위치하는 디렉토리의 절대 경로
- MEDIA_URL
    - MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
    - STATIC_URL과 동일한 역할
```python
# setting.py

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = 'media/'
```
- MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
    - 업로드 된 파일의 URL == settings.MEDIA_URL
    - 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
#### 업로드
- model에 image field를 추가
```python
# articles/models.py

class Article(models.Model):
    # 기존 model에 image 테이블 추가
    # blank=True: 빈 문자열이 저장되도록 허용
    image = models.ImageField(blank=True)
```
- migration 진행
```bash
# ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요
$ pip install Pillow
$ pip freeze > requirements.txt

$ python manage.py makemigrations
$ python manage.py migrate
```
- form 요소의 enctype 속성 추가
```html
<form action="{% url "articles:create" %}" method="POST" enctype="multipart/form-data">
```
- view 함수 업로드 파일에 대한 추가 코드 작성
    - 파일은 POST로 받을 수 없음
```python
def create(request):
    if request.method == 'POST':
        # 파일을 받을 인자 추가
        form = ArticleForm(request.POST, request.FILES)
    ...
```
- DB에는 파일에 대한 경로가 문자열로 저장됨
    - 경로를 활용해서 사용자에게 출력

#### 업로드 이미지 제공하기
- 'url'속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
```html
<!-- articles/detail.html -->

<!-- 이미지를 업로드하지 않은 경우 detail 템플릿이 렌더링 되지 않음 -->
<!-- 이미지 데이터가 있는 경우에만 출력하도록 처리 -->
{% if article.image %}
  <img src="{{ article.image.url }}" alt="#">
{% endif %}
```

#### 업로드 이미지 수정
- 수정 페이지 form 요소에 enctype 속성 추가
```html
<!-- articles/update.html -->

<form action="{% url "articles:update" article.pk %}" method="POST" enctype="multipart/form-data">
```
- update view 함수에서 업로드 파일에 대한 추가 코드 작성
```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
    ...
```

## 참고
### 'upload_to' argument
- ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정
```python
# articles/models.py

# media 안에 저장할 폴더 설정
#1 images 폴더
image = models.ImageField(blank=True, upload_to='images/')
#2 년/월/일 폴더
image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
# 함수를 생성하여 지정할 수 있음 (ex.유저 이름별 폴더)
```