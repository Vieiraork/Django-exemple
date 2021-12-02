from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloWordl),
    path('', views.contas, name='contas'),
]
