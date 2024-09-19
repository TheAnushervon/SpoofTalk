from django.db import models

# Create your models here.


class Message(models.Model):
    text = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
