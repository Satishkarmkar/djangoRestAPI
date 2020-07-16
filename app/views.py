from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import AdminModel
from app.models import AddCourseModel

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
        return redirect('adminlogin')

def addNewCourse(request):

    return render(request,'add_new_course.html')

def saveCourse(request):
    courseno = request.POST.get("c0")
    coursename = request.POST.get("c1")
    facultyname = request.POST.get("c2")
    coursedate = request.POST.get("c3")
    coursetime = request.POST.get("c4")
    coursefee = request.POST.get("c5")
    coursedur = request.POST.get("c6")
    # print(courseno, coursename, facultyname, coursedate, coursetime, coursefee, courasedur)
    AddCourseModel(cno=courseno, cname=coursename, fname=facultyname, cdate=coursedate, ctime=coursetime, fee=coursefee,dur=coursedur).save()
    messages.success(request,"New Course Added")
    return redirect('addnewcourse')

def viewAllCourse(request):
    coursedata = AddCourseModel.objects.all()
    # print(coursedata)
    return render(request,"view_all_courses.html",{"data":coursedata})

def editCourse(request):
    data = AddCourseModel.objects.all()
    return render(request,'editcourse.html',{"data":data})

def saveEdit(request):
    courseno = request.GET.get("c0")

    courseno = request.POST.get("c0")
    coursename = request.POST.get("c1")
    facultyname = request.POST.get("c2")
    coursedate = request.POST.get("c3")
    coursetime = request.POST.get("c4")
    coursefee = request.POST.get("c5")
    coursedur = request.POST.get("c6")

    AddCourseModel.objects.filter(cno=courseno).update(cno=courseno, cname=coursename, fname=facultyname, cdate=coursedate, ctime=coursetime, fee=coursefee,dur=coursedur)
    return redirect('viewallcourse')

def adminLogout(request):
    return render(request,'admin_login.html')

