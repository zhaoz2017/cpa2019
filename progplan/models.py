from django.db import models

# Create your models here.
class Main_plan(models.Model):
    mplan_name = models.CharField(max_length=50)
    mreq_num = models.IntegerField()
    msub = models.CharField(max_length=30)
    mnum = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    def __str__(self):
        return self.userid

class Option_plan(models.Model):
    oplan_name = models.CharField(max_length=50)
    oreq_num = models.IntegerField()
    osub = models.CharField(max_length=30)
    onum = models.CharField(max_length=30)
    oname = models.CharField(max_length=30)
    def __str__(self):
        return self.oplan_name
