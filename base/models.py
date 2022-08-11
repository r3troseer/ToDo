from timeit import repeat
from unicodedata import name
from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Reapeat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    slug = AutoSlugField(populate_from="name", null=True)
    due_date = models.DateField
    due_time = models.TimeField
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    repeat = models.ForeignKey(Reapeat, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
