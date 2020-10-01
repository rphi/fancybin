from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Paste(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=50)
  content = models.TextField(default="empty paste")
  language = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  private = models.BooleanField(default=False)
