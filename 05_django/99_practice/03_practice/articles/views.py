from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시글 정보 요청
    # Class.manager.QuerySet API
    # <QuerySet []>
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)