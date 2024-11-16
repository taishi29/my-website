from django.urls import path
from . import views
from .views import ContactView, ThanksView

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='intro'),
    path('work/', views.work, name='work'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('health-check/', views.health_check, name='health_check')
]
