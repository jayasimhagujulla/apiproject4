from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    roolno=models.IntegerField()
    marks=models.IntegerField()
    gf=models.CharField(max_length=30)
    bf=models.CharField(max_length=30)
    