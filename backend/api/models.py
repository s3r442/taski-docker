"""Task model definitions."""

from django.db import models


class Task(models.Model):
    """Simple task model with title, description and status."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        """Return task title as its string representation."""
        return self.title
