from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus,
    }
    return render(request, 'menus/index.html', context)


def create(request):
    return render(request, 'menus/create.html')