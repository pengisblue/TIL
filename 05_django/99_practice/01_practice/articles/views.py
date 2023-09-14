from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'greeting': '반갑습니다.'
    }
    return render(request, 'articles/index.html', context)


def random_number(request, number):
    next_number = number + 1
    context = {
        'number': number,
        'next_number': next_number,
    }
    return render(request, 'articles/random_number.html', context)