from django.urls import path
from . import views

urlpatterns = [
    path('trash_notifier/', views.notify_trash, name='trash_notifier'),
]