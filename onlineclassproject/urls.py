"""OnlineClassSchedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('adminlogin/',views.adminLogin, name = 'adminlogin'),

    path('validateadmin/',views.validateAdmin,name = 'validateadmin'),

    path('adminwelcome/',views.adminWelcome,name = 'adminwelcome'),

    path('addnewcourse/',views.addNewCourse,name = 'addnewcourse'),

    path('savecourse/',views.saveCourse,name = 'savecourse'),

    path('viewallcourse/',views.viewAllCourse,name = 'viewallcourse'),

    path('editcourse/<int:pk>/',views.editCourse,name = 'editcourse'),

    path('saveedit/',views.saveEdit,name = 'saveedit'),

    path('deletecourse/<int:pk>/',views.deleteCourse,name='deletecourse'),

    path('adminlogout/',views.adminLogout,name = 'adminlogout'),

    path('studentregistration/',views.studentRegistration,name= 'studentregistration'),

    path('saveregistration/',views.saveRegistration,name= 'saveregistration'),

    path('studenthome/',views.studentHome,name='studenthome'),

    path('enrollcourse/',views.enrollCourse,name='enrollcourse'),

    # path('getcourse/',views.getCourse,name='getcourse'),

    path('viewallenrolledcourse/',views.viewAllEnrolledCourse,name='viewallenrolledcourse'),

    path('cancelenrolledcourse/',views.cancelenrolledcourse,name='cancelenrolledcourse')
    ]
