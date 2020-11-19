from django.shortcuts import render, redirect
from .models import NewTask
from django.http import HttpResponse
from .forms import TaskForm


# Create your views here.
def home(request):
    tasks = NewTask.objects.all()
    content = {"tasks": tasks}
    return render(request, "ToDo/main.html", content)
def task_update(request,pk):
    task = NewTask.objects.all().filter(id=pk)[0]
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("home")
    form = TaskForm(instance=task)
    content = {'form': form}
    return render(request, 'ToDo/update.html',content)
def new_task(request):
    task = NewTask.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    form = TaskForm()
    content = {'form': form}
    return render(request, "ToDo/newtask.html",content)
def see_task(request,pk):
    task = NewTask.objects.all().filter(id=pk)[0]
    form = TaskForm(request.POST, instance=task)
    form = TaskForm(instance=task)
    content = {'form': form}
    return render(request, 'ToDo/seetask.html',content)
def delete_task(request,pk):
    task = NewTask.objects.get(id=pk)
    task.delete()
    return render(request, 'ToDo/delete.html')
