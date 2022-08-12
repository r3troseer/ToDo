from ast import Delete
from venv import create
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<str:pk>/<slug:slug>", views.detail, name="detail"),
    
    path('dashboard/', views.dashboard, name="dashnoard"),

    path('create/', views.createTask, name="create"),
    path('update/<str:pk>/', views.updateTask, name="update"),
    path('delete/<str:pk>', views.deleteTask, name="delete")
]
