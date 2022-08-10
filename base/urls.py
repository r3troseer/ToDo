from ast import Delete
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<str:pk>/<slug:slug>", views.detail, name="detail"),
    path('delete/<str:pk>', views.deleteTask, name="delete")
]
