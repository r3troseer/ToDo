from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Priority, Task, Tag
from .forms import TaskForm


# view function form the homepage where all tasks are viewed
def home(request):
    tasks = Task.objects.all
    if request.GET.get("q") is not None:
        q = request.GET.get("q")
    else:
        q = ""
    tasks = Task.objects.filter(
        Q(tag__name__icontains=q) | Q(priority__name__icontains=q)
    )
    tags = Tag.objects.all
    priorities = Priority.objects.all
    context = {"tasks": tasks, "tags": tags, "priorities": priorities}
    return render(request, "home.html", context)


# view function to view more details about selected task
def detail(request, pk, slug):
    task = Task.objects.get(id=pk, slug=slug)
    context = {"task": task}
    return render(request, "details.html", context)


# view function to show data of finished and un finshed task in graph
def dashboard(request):
    return render(request)


# view function to create task
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


# view function to edit tasks
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TaskForm(instance=task)
    # messages.success(request, "task created")

    context = {"form": form}
    return render(request, "create.html", context)


# view function to delete tasks
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "task deleted")
        return redirect("home")

    context = {"task": task}
    return render(request, "delete.html", context)
