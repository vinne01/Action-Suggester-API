from django.db import models
from django.utils import timezone

class QueryLog(models.Model):
    query = models.TextField()
    tone = models.CharField(max_length=100)
    intent = models.CharField(max_length=100)
    suggested_actions = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)

