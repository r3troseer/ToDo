from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
