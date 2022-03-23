from django.urls import path
from . import views

app_name = 'buymeacoffee'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
]