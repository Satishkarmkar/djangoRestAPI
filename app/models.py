from django.db import models
# Create your models here.
class LoginModel(models.Model):
    uname = models.CharField(max_length=10)
    upass = models.CharField(max_length=10)
    type = models.CharField(max_length=10,default=None)

class AddCourseModel(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    cdate = models.DateField()
    ctime = models.TimeField()
    fee = models.FloatField()
    dur = models.IntegerField()


class StudentRegistrationModel(models.Model):
    sidno = models.CharField(max_length=10,primary_key=True)
    sname = models.CharField(max_length=30)
    semail = models.EmailField(max_length=50)
    smobno = models.IntegerField()
    sgender = models.CharField(max_length=7)
    sdob = models.DateField()
    saddrs = models.CharField(max_length=100)
    scity = models.CharField(max_length=40)
    spincode = models.IntegerField()
    sstate = models.CharField(max_length=30)
    scountry = models.CharField(max_length=30)
    uname = models.CharField(max_length=10,default=None)
    upass = models.CharField(max_length=10,default=None)
    type = models.CharField(max_length=10,default=None)

class StudentEnrolledCourseModel(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=20)
    smobno = models.IntegerField(default=True)





