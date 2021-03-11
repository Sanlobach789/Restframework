from django.db import models
from django.utils import timezone

from authapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    git_link = models.TextField(blank=True)
    related_users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    updated = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
