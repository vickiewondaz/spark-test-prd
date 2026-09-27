from django.contrib.auth.models import User
from django.db import models


class Idea(models.Model):
    STAGES = [
        ('ideas', 'Ideas'),
        ('planning', 'Planning'),
        ('building', 'Building'),
        ('testing', 'Testing'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ideas')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    stage = models.CharField(max_length=20, choices=STAGES, default='ideas')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']


class Note(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Milestone(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='milestones')
    label = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
