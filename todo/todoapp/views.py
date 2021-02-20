from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
    if request.method=='POST':
        form=TodoForm(request.POST,request.FILES)
        if form.is_valid:
            newtodo=Todo(user=request.user,title=request.POST['title'],status=False)
            newtodo.save()
            return HttpResponseRedirect(reverse('todoapp:index',))
        else:
            return HttpResponseRedirect(reverse('todoapp:index', ))
            
    else:
        form=TodoForm()
            
        
    context={'form':form}
    return render(request,'new.html',context)

def edit(request,todo_id):
    todo = get_object_or_404(Todo,id=todo_id)
    todo.status = True
    todo.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
def delete(request,todo_id):
    todo = get_object_or_404(Todo,id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))
    