from django.contrib import admin
from .models import Task, Priority, Tag, Repeat

admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(Tag)
admin.site.register(Repeat)
