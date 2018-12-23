from django.db import models

# Create your models here.

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(blank=True)
