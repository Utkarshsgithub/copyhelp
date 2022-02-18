from email import contentmanager
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class COPY(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)