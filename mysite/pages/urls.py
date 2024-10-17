from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='intro'),
    path('contact/', views.contact, name='contact'),    
]
