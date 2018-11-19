from django.db import models

# Create your models here.
class Ctcs2(models.Model):
    Course_number = models.CharField(max_length=8)

    def __str__(self):
        return self.Course_number
