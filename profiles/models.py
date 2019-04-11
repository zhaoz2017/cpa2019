from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(max_length=70)
    gender = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)
    starting_semester = models.CharField(max_length=20, blank=True)
    starting_year = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=70, blank=True)
    progplan = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.first_name

class User_prog_plan(models.Model):
    userid = models.CharField(max_length=30)
    ureq_num = models.IntegerField()
    met_flag = models.IntegerField()
    usub = models.CharField(max_length=30)
    unum = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)

    def __str__(self):
        return self.userid
