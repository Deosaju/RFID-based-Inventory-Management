from django.db import models
import serial

class MyData(models.Model):
    pid = models.CharField(max_length=100)
    serial= models.CharField(max_length=100 , default='error')
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
            