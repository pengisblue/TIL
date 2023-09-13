from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def info(request):
    return render(request, 'pages/info.html')


def skills(request):
    return render(request, 'pages/skills.html')


def projects(request):
    return render(request, 'pages/projects.html')


def contacts(request):
    return render(request, 'pages/contacts.html')