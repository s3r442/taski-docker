"""Serializers for API models."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model fields used in the API."""

    class Meta:
        """Meta options for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
