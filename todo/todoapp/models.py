from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    title=models.CharField('Topshiriq nomi',max_length=100)
    status=models.BooleanField('Topshiriq holati',default=False)
    
    def __str__(self):
        return self.user.username