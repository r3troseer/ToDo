from django.db import models
from autoslug import AutoSlugField
from datetime import date, time


class Priority(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Repeat(models.Model):
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
    due_date = models.DateField(("Date"), default=date.today)
    due_time = models.TimeField(("Time"), default=time)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    repeat = models.ForeignKey(Repeat, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
