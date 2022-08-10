from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    slug = AutoSlugField(populate_from="name", null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
