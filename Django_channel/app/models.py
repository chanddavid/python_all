from tkinter import CASCADE
from django.db import models
from sqlalchemy import true

# Create your models here.
class ChatModel(models.Model):
    content=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE)

class Group(models.Model):
    name=models.CharField(max_length=100)

