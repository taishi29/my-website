from django.urls import path
from . import views

urlpatterns = [
    path('', views.trash_notify, name='trash_notifier'),
]