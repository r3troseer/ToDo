from django import forms
from .models import Task


# task form to create or edit tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
