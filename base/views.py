from asyncio import tasks
from email import message
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Priority, Task

# Create your views here.


def home(request):
    tasks = Task.objects.all
    context = {"tasks": tasks}
    return render(request, "home.html", context)


def detail(request, pk, slug):
    task = Task.objects.get(id=pk, slug=slug)
    context = {"task": task}
    return render(request, "details.html", context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("home")
    messages.info(request, "task deleted")

    context = {"task": task}
    return render(request, "delete.html", context)
