from django.shortcuts import render
from .models import Todo
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