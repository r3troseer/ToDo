from django.contrib import admin

# Register your models here.
from .models import Task, Priority, Tag, Repeat

admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(Tag)
admin.site.register(Repeat)
