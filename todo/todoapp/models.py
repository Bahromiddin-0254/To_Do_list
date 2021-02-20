from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField('Topshiriq nomi',max_length=100)
    status=models.BooleanField('Topshiriq holati',default=False)

    def __str__(self):
        return self.user.username
    def get_edit(self):
        return reverse('todoapp:edit', kwargs={'todo_id':self.id})
    def get_del(self):
           return reverse('todoapp:delete', kwargs={'todo_id':self.id})
    