from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Priority, Task
from .forms import TaskForm

# Create your views here.


def home(request):
    tasks = Task.objects.all
    context = {"tasks": tasks}
    return render(request, "home.html", context)


def detail(request, pk, slug):
    task = Task.objects.get(id=pk, slug=slug)
    context = {"task": task}
    return render(request, "details.html", context)


def dashboard(request):
    return render(request)


def createTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            return redirect("home")
    else:
        form = TaskForm

    context = {"form": form}
    return render(request, "create.html", context)


def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    
    context = {"form": form}
    return render(request, "create.html", context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("home")
    messages.info(request, "task deleted")

    context = {"task": task}
    return render(request, "delete.html", context)
