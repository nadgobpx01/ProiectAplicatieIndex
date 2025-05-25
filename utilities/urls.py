from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_consumption, name='add_consumption'),
]