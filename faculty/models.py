from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Solution(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body_q = models.TextField()
    body_a = models.TextField()
    votes_total = models.IntegerField(default=1)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
