from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User 


def home(request):
    todo = Todo.objects.filter(created_by=request.user)[0:5]
    context={'todo':todo}
    return render(request, 'home.html', context)


def createTask(request):
    if request.method=='POST':
        title = request.POST["task"]
        date = timezone.now()
        created_by=request.user
        new_task = Todo(created_by=created_by, title=title, date=date)
        new_task.save()
        messages.success(request,'Task successfully added!')
        return redirect('home')
    return render(request, 'add-task.html',{})

def deleteTask(request, pk):
    item = Todo.objects.get(id=pk)
    context={'item':item}
    if request.method=='POST':
        item.delete()
        messages.error(request,'Task successfully deleted!')
        return redirect('home')
    return render(request, 'delete.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f' Welcome {username}!')
            return redirect('home')
        else:
            messages.info(request, f'Incorrect username or password!')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username taken, try a new one!')
            else:
                user= User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Account created successfully!')
                auth.login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Password doesn't match!")
    return render(request, 'register.html')