from django.db import models
from autoslug import AutoSlugField
from datetime import date, time

Priority_list = (
    ("low priority", "low priority"),
    ("Normal", "Normal"),
    ("high priority", "high priority"),
)

Repeat_list = (
    ("Repeat Once", "Repeat Once"),
    ("Repeat Daily", "Repeat Daily"),
    ("Repeat Weekly", "Repeat Weekly"),
    ("Repeat Monthly", "Repeat Monthly"),
)


class Priority(models.Model):
    name = models.CharField(max_length=20, choices=Priority_list, default="Normal")

    def __str__(self):
        return self.name


class Repeat(models.Model):
    name = models.CharField(max_length=20, choices=Repeat_list, default="Repeat Once")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200, default="Task name")
    description = models.TextField(max_length=500, default="task details")
    slug = AutoSlugField(populate_from="name", null=True)
    date = models.DateField(("Date"), default=date.today)
    time = models.TimeField(("Time"), default=time)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    repeat = models.ForeignKey(Repeat, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
