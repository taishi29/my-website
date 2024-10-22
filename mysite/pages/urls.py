from django.urls import path
from . import views
from .views import ContactView

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='intro'),
    path('work/', views.work, name='work'),
    path('contact/', ContactView.as_view(), name='contact'),
]
