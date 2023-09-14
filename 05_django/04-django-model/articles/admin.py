from django.contrib import admin
# 명시적 상대경로
from .models import Article

# Register your models here.

# Article 모델 클래스를  admin site에 등록
# admin site에 등록(register)한다
admin.site.register(Article)