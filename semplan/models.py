from django.db import models
from django.db.models import Q


# Create your models here.
class Course(models.Model):
    crn = models.PositiveIntegerField(primary_key = True)  #PositiveInt
    sub = models.CharField(max_length = 3)  #CharField
    num = models.CharField(max_length = 4)  #CharField
    title = models.CharField(max_length = 255)  #TextField
    section = models.CharField(max_length = 3)  #CharField
    prof = models.CharField(max_length = 255)    #TextField
    cred = models.PositiveSmallIntegerField()    #PositiveSmallInt?
    sem = models.CharField(max_length = 7)  #CharField
    max_enroll = models.PositiveSmallIntegerField()  #PositiveSmallInt?
    actual_enroll = models.PositiveSmallIntegerField()   #PositiveSmallInt?

    def __str__(self):
        return "{} | {} {} - {}:\nSection: {} Instructor: {} Credit Hours: {} Semester: {} Max Enroll: {} Actual Enroll: {}\n".format(
                self.crn, self.sub, self.num, self.title,
                self.section, self.prof, self.cred,
                self.sem, self.max_enroll, self.actual_enroll)

class Meeting(models.Model):
    crn = models.ForeignKey(Course, to_field='crn', on_delete = models.CASCADE)
    begin_time = models.PositiveIntegerField()   #CharField
    end_time =models.PositiveIntegerField()   #CharField
    days = models.CharField(max_length = 7) #CharField
    building = models.CharField(max_length = 6)#CharField
    room = models.CharField(max_length = 4) #CharField

    def __str__(self):
        return "Days: {} Begin Time: {} End Time: {} Building: {} Room: {}\n".format(
                self.days, self.begin_time, self.end_time,
                self.building, self.room)
'''
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    scheduleNum = models.PositiveSmallIntegerField()    # need restriction 1-5 only on this

    def __str__(self):
        return self.first_name

class Schedule(models.Model):
    crn = models.ForeignKey(Course, to_field='crn', on_delete = models.CASCADE)
    user = models.ForeignKey(Profile, to_field='email', on_delete = models.CASCADE)
    userSchedNum = models.PositiveSmallIntegerField()   # need restriction 1-5 only on this
    userSchedClassNum = models.PositiveSmallIntegerField()   # need restriction 1-10 only on this

'''

'''
class prerequisite(model.Models):
    course = #CharField
    prerequisite = #CharField
'''
