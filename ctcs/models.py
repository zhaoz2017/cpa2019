from django.db import models

# Create your models here.
class Ctcs(models.Model):
    Registration_year = models.CharField(max_length=10)
    Registration_semeter = models.CharField(max_length=10)
    major = models.CharField(max_length=30)
