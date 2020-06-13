from django.db import models

# Create your models here.

class bilder(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='bilder pic')
    desc = models.TextField()

