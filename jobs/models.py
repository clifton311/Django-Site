from django.db import models

# Create your models here.
class Job(models.Model):
  image = models.ImageField(upload_to='images/')
  # all models are saved to one directory
  summary = models.CharField(max_length=200)

