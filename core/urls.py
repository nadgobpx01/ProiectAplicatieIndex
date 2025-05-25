from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.public_home, name='public-home'),
    path('dashboard/', views.home, name='home'),  # doar după login
    path('about/', views.about, name='about'),

]
