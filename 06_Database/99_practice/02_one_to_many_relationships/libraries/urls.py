from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:author_pk>/books/create/', views.create_book, name='create_book'),
]
