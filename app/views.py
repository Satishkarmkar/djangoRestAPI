from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import AdminModel,AddCourseModel

# Create your views here.

def adminLogin(request):
    return render(request,"admin_login.html")


def adminWelcome(request):
    return render(request,"admin_welcome.html")


def validateAdmin(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")

    try:
        AdminModel.objects.get(uname = uname, upass=upass)
        return render(request,"admin_welcome.html")
    except AdminModel.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect('admin_login')

def addNewCourse(request):
    cno = request.POST.get("c0")
    cname = request.POST.get("c1")
    fname = request.POST.get("c2")
    cdate = request.POST.get("c3")
    ctime = request.POST.get("c4")
    fee = request.POST.get("c5")
    dur = request.POST.get("c6")
    print((cno,cname,fname,cdate,ctime,fee,dur))
    course = AddCourseModel(cno=cno,cname=cname,fname=fname,cdate=cdate,ctime=ctime,fee=fee,dur=dur)
    course.save()
    return redirect('add_new_course')


def adminLogout(request):
    return render(request,'admin_login.html')

