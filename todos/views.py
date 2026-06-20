from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def registerPage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = UserCreationForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    context = {"form": form}
    return render(request, "registration/register.html", context)

@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.all()
    search_query = request.GET.get("search")
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    context = {"tasks" : tasks}
    return render(request , "todos/home.html", context)

@login_required(login_url='login')
def create_task(request):
    if request.method == "POST":
        task = request.POST.get("title")
        Task.objects.create(title=task)    
        return redirect("task_list")

@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("task_list")

@login_required(login_url='login')
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.is_done = "is_done" in request.POST
        task.save()
        return redirect("task_list")
    context = {"task": task}
    return render(request, "todos/update_task.html", context)



















































































