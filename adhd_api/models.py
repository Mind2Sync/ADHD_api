from django.db import models
from django.utils import timezone

class MRIPrediction(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    prediction = models.FloatField(default=0)  
    mriScan = models.FileField(upload_to='mri_scans') 
