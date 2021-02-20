from django.urls import path
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('',index,name='index'),
    path('profile/',profile,name='profile'),
    path('new/',new,name='new'),
    path('edit/<int:todo_id>',edit,name='edit'),
    path('delete/<int:todo_id>',delete,name='delete'),
]
