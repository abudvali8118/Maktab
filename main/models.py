from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Zapallar(models.Model):
    ism = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.ism