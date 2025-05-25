from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_main_menu, name='user_main_menu'),
]

