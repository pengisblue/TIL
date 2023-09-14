from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # variable routing
    path('<int:number>/', views.random_number, name='random_number'),
]
