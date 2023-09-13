import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    empty_list = []
    context = {
        'foods': foods,
        'picked': picked,
        'empty_list': empty_list
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # print(request)  # <WSGIRequest: GET '/catch/?message=%EB%B0%A9%EA%B0%80%EB%B0%A9%EA%B0%80'>
    # print(type(request))    # <class 'django.core.handlers.wsgi.WSGIRequest'>
    # print(request.GET)  # <QueryDict: {'message': ['방가방가']}>
    # print(request.META)
    # 사용자로 부터 요청(request)을 받아서
    # 요청에서 사용자 입력 데이터를 찾아
    # context에 저장 후 catch 템플릿에 출력
    print(request.GET.get('message'))   # 방가방가
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/gretting.html', context)


def detail(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)