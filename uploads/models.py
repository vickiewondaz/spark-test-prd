import uuid

from django.db import models

from ideas.models import Idea


def upload_path(instance, filename):
    ext = filename.split('.')[-1] if '.' in filename else 'bin'
    return f"uploads/{uuid.uuid4().hex}.{ext}"


class Attachment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to=upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
