"""Admin registration for Task model."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin for Task model showing main fields."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
