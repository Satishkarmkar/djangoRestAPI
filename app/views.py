from django.shortcuts import render,redirect
from django.contrib import messages

from app.models import LoginModel,AddCourseModel,StudentRegistrationModel,StudentEnrolledCourseModel

# Create your views here.

def adminLogin(request):
    return render(request,"admin_login.html")


def adminWelcome(request):
    return render(request,"admin_welcome.html")


def validateAdmin(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")
    type = request.POST.get("t3")
    # stu_uname = request.POST.get("s11")
    # stu_passwd = request.POST.get("s12")
    # stype = "student"
    
    try:
        if uname =="satish" and upass =="Satish@3118" and type =="admin":
            LoginModel.objects.get(uname=uname, upass=upass, type=type)
            return render(request,"admin_welcome.html")
        elif uname == uname and upass == upass and type == type:
            StudentRegistrationModel.objects.get(uname=uname, upass=upass, type=type)
            return render(request,"studenthome.html")
    except LoginModel.DoesNotExist:
        messages.error(request,"Invalid User Credentials")
        return redirect('adminlogin')
    except StudentRegistrationModel.DoesNotExist:
        messages.error(request,"Invalid User Credentials")
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

def editCourse(request,pk):

    cdata=AddCourseModel.objects.get(pk=pk)
    return render(request,"editcourse.html",{"cordata":cdata})

def saveEdit(request):
    # courseno = request.GET.get("c0")

    courseno = request.POST.get("c0")
    coursename = request.POST.get("c1")
    facultyname = request.POST.get("c2")
    coursedate = request.POST.get("c3")
    coursetime = request.POST.get("c4")
    coursefee = request.POST.get("c5")
    coursedur = request.POST.get("c6")

    AddCourseModel.objects.filter(cno=courseno).update(cno=courseno, cname=coursename, fname=facultyname, cdate=coursedate, ctime=coursetime, fee=coursefee,dur=coursedur)
    return redirect('viewallcourse')

def deleteCourse(request,pk):
    AddCourseModel.objects.get(pk=pk).delete()
    return redirect('viewallcourse')

def adminLogout(request):
    return render(request,'admin_login.html')




#******************Student Section********************

def studentRegistration(request):
    return render(request,"studentregistration.html")

def saveRegistration(request):
    stu_id = request.POST.get("s0")
    stu_name = request.POST.get("s1")
    stu_mail = request.POST.get("s2")
    stu_mob = request.POST.get("s3")
    stu_gender = request.POST.get("s4")
    stu_dob = request.POST.get("s5")
    stu_addrs = request.POST.get("s6")
    stu_city = request.POST.get("s7")
    stu_pincode = request.POST.get("s8")
    stu_state = request.POST.get("s9")
    stu_country = request.POST.get("s10")
    stu_uname = request.POST.get("s11")
    stu_passwd = request.POST.get("s12")
    stu_cnpasswd = request.POST.get("s13")
    stype = "student"

    if stu_passwd == stu_cnpasswd:
        StudentRegistrationModel(sidno=stu_id,sname=stu_name,semail=stu_mail,smobno=stu_mob,sgender=stu_gender,sdob=stu_dob,saddrs=stu_addrs,scity=stu_city,spincode=stu_pincode,sstate=stu_state,scountry=stu_country,uname=stu_uname,upass=stu_passwd,type=stype).save()
        LoginModel(uname=stu_uname,upass=stu_passwd,type=stype).save()
        messages.success(request,"Thank You for Registration")
        return render(request, "admin_login.html")
    else:
        messages.error(request,"Please Check Confirm Password")
        return redirect('studentregistration')


def studentHome(request):
    return render(request,"studenthome.html")


#**********************Student Course Enrollment Section*******************

def enrollCourse(request):
    stu_mob = request.GET.get("s3")
    cdata = AddCourseModel.objects.all()
    # availcoursedata = AddCourseModel.objects.all()
    return render(request,"enroll_course.html",{ "data":cdata,"studata":stu_mob })
#
# def getCourse(request):
#     # enroll = AddCourseModel.objects.all()
#     # stu_mob = request.POST.get("s3")
#     # try:
#     #     courseno = request.POST.get("c0")
#     #     StudentEnrolledCourseModel(smobno = stu_mob,cno = courseno).save()
#     #     messages.success(request,"Enrolled Successfully")
#     #     return redirect('viewallenrolledcourse', {'contact': stu_mob, 'ecourse': enroll})
#     # except:
#     #     messages.error(request,"Already Enrolled")
#     #     return redirect('enrollcourse',{'contact':stu_mob,'ecourse':enroll})
#
#
#     enroll = AddCourseModel.objects.all()
#     stu_mob = request.POST.get("s3")
#
#     try:
#         courseno = request.POST.get("c0")
#         coursename = request.POST.get("c1")
#         StudentEnrolledCourseModel(smobno=stu_mob,cname=coursename,cno=courseno).save()
#         return render(request,'view_all_enrolled_course.html', {'contact': stu_mob, 'ecourse': enroll})
#     except:
#         return render(request,'studenthome.html')



def viewAllEnrolledCourse(request):
    availcoursedata = StudentEnrolledCourseModel.objects.all()
    return render(request,"view_all_enrolled_course.html",{"data":availcoursedata})

def cancelenrolledcourse(request):
    return render(request,"cancel_enrolled_course.html")
