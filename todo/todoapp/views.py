from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    try:
        todos = Todo.objects.filter(user=request.user)
        context = {'todos':todos}
    except:
        context ={}
    return render(request,'index.html',context)



def profile(request):
    return render(request,'profile.html')
@login_required
def new(request):
    user =User.objects.filter(username=request.user)
    if request.method=='POST':
        form=TodoForm(request.POST,request.FILES)
        form.user=user
        form.status=False
        if form.is_valid:
            form.save()
            HttpResponseRedirect(reverse('todoapp:index'))
        else:
            return HttpResponseRedirect(reverse('todoapp:new' ))
    else:
        form=TodoForm()
    context={'form':form}
    return render(request,'new.html',context)