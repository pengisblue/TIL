# 10/5 강의
## 회원가입
- User 객체를 Create 하는 과정

### UserCreationForm()
- 회원가입시 사용자 입력 데이터를 받을 built-in `ModelForm`
    - 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스
    ```python
    class Meta:
        model = User
    ```
- CustomUserCreationForm()
    - 커스텀 유저 모델을 사용하기 위해서 UserCreationForm()을 상속받는 커스텀 폼
- get_user_model()
    - 현재 프로젝트에서 `활성화된 사용자 모델`을 반환하는 함수
    - 커스텀 User 모델을 자동으로 반환해줌
        - User 모델에 변경사항이 생겨도 코드를 수정할 필요가 없어짐

#### CustomUserCreationForm()
```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    # UserCreationForm의 Meta를 상속 받으면서 model만 오버라이드
    class Meta(UserCreationForm.Meta):
        # User클래스를 직접 참조하지 않고 get_user_model()을 사용해 참조
        model = get_user_model()
```

### 회원가입 페이지 작성
```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

```html
<!-- accounts/signup.html -->

<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```

### 회원가입 로직작성
```python
# accounts/views.py

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(requset, 'accounts/signup.html', context)
```

## 회원탈퇴
- User 객체를 Delete하는 과정

### 회원탈퇴 로직
```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('delete/', views.delete, name='delete')
]
```

```python
# accounts/views.py

def delete(request):
    request.user.delete()
    return redirect('aritlces:index')
```

```html
<!-- accounts/index.html -->

<form action="{% url 'accounts:delete' %}" method="POST">
  {% csrf_token %}
  <input tupe="submit" value="회원탈퇴">
</form>
```

## 회원정보 수정
- User 객체를 Update하는 과정

### UserChangeForm()
- 회원정보 수정 시 사용자 입력 데이터를 받을 built-in `ModelForm`
- CustomUserChangeForm()
    - 커스텀 유저 모델을 사용하기 위해서 UserChangeForm()을 상속받는 커스텀 폼

#### CoutomUserChangeForm()
```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```

### 회원정보 수정 페이지 작성
```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('update/', views.update, name='update'),
]
```

```python
# accounts/views.py

from .forms import CustomUserChangeForm


def update(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserChangeForm(instance=reqeust.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```html
<!-- accounts/update.html -->

<h1>회원정보 수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token%}
  {{ form.as_p }}
  <input type='submit'>
</form>
```

```html
<!-- articles/index.html -->

<a href="{% url 'accounts:update' %}">회원정보 수정</a>
```

#### UserChangeForm 사용 시 문제점
- 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야함
    - CustomUserChangeForm에서 접근 가능한 필드를 조정

#### CustomUserChangeForm 출력 필드 재정의
```python
# accounts/forms.py

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
```

### 회원정보 수정 로직 작성
```python
# accounts/views.py

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=reqeust.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

## 비밀번호 변경
- 인증된 사용자의 Session 데이터를 Update 하는 과정
- django는 비밀번호 변경 페이지를 회원정보 수정 form에 별도 주소로 안내
    - /user_pk/password/

### PasswordChangeForm()
- 비밀번호 변경 시 사용자 입력 데이터를 받을 built-in `Form`

### 비밀번호 변경 페이지 작성
```python
# crud/urls.py

from accounts import views

urlpatterns = [
    ...,
    path('<int:user_pk>/password/', views.change_password, name='change_password'),
]
```

```python
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm


def change_password(requset, user_pk):
    if reqeust.method == 'POST':
        pass
    else:
        form = PasswordChangeForm(reqeust.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

```html
<!-- accounts/change_password.html -->

<h1>비밀번호 변경</h1>
<form action="{% url 'change_password' user.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```

### 비밀번호 변경 로직 작성
```python
# accounts/views.py

def change_password(requset, user_pk):
    if reqeust.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(reqeust.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

### 세션 무효화 방지하기
#### 암호변경 시 세션 무효화
- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치않게 되어 로그아웃 처리됨

#### update_session_auth_hash(reqeust, user)
- 암호변경 시 세션 무효화를 막아주는 함수
    - 암호가 변경되면 새로운 password의 Sesseion Data로 기존 session을 자동으로 갱신
```python
# accounts/views.py

from django.contrib.auth import update_session_auth_hash


def change_password(requset, user_pk):
    if reqeust.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # 변경된 부분
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(reqeust.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

## 인증된 사용자에 대한 접근 제한
### 1. is_authenticated 속성
- 사용자가 인증되었는지 여부를 알 수 있는 User model의 속성
> 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이며, 비인증 사용자에 대해서는 항상 False

#### 적용
- 로그인과 비로그인 상태에서 화면에 추력되는 링크를 다르게 설정하기
```html
<!-- articles/index.html -->

<h1>INDEX</h1>
{% comment %} {% if user.is_authenticated %} {% endcomment %}
<!-- 위와 아래는 같지만, django는 request.user로 표현할 것을 권장 -->
{% if request.user.is_authenticated %}
  <h3>{{ user.username }}님 안녕하세요!</h3>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="LOGOUT">
  </form>
  <form action="{% url 'accounts:delete' %}">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
  </form>
  <a href="{% url 'accounts:update' %}">회원정보수정</a>
{% else %}
  <a href="{% url 'accounts:login' %}">LOGIN</a>
  <a href="{% url 'accounts:signup' %}">SIGNUP</a>
{% endif %}
```

- 인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기
```python
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...
```

### 2. login_required 데코레이터
- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
> 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴

```python
# accounts/views.py

from django.contrib.auth.decorators import login_required


@login_required
def logout(request):
    pass

@login_required
def delete(request):
    pass

@login_required
def update(request):
    pass

@login_required
def change_password(request, user_pk):
    pass
```