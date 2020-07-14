from django.db import models
# Create your models here.
class AdminModel(models.Model):
    uname = models.CharField(max_length=10)
    upass = models.CharField(max_length=10)

class AddCourseModel(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    cdate = models.DateField()
    ctime = models.TimeField()
    fee = models.FloatField()
    dur = models.IntegerField()
