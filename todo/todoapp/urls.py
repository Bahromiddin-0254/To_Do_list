from django.urls import path
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('',index,name='index'),
    path('profile/',profile,name='profile'),
]
