from django import forms
from django.forms import fields
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields=('title','status')