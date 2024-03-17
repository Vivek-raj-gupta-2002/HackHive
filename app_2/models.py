from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Follower(models.Model):
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    areaofexpertise = models.CharField(max_length=100)
    addyourcalendylink = models.URLField()
    about = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    