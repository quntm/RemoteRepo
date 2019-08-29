from django.shortcuts import render,redirect
from .models import Registration
from .forms import RegistrationForm,Login
from django.http.response import HttpResponse

def Reg_View(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            mobile=request.POST.get("mobile")
            email=request.POST.get("email")
            username=request.POST.get("username")
            password=request.POST.get("password")

            data=Registration(
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                email=email,
                username=username,
                password=password
            )

            data.save()
            rform=RegistrationForm()
            return render(request,"Reg.html",{'rform':rform})
        else:
            return HttpResponse("Invalid data")


    else:
        rform=RegistrationForm()
        return render(request,"Reg.html",{'rform':rform})


def Login_View(request):
    if request.method=="POST":
        lform=Login(request.POST)
        if lform.is_valid():
            uname=request.POST.get("username")
            pwd=request.POST.get("password")

            username1=Registration.objects.filter(username=uname)
            pwd1=Registration.objects.filter(password=pwd)

            if username1 and pwd1:
                return HttpResponse("Login successful")
            else:
                return HttpResponse("invalid login")
        else:
            return HttpResponse("INVALID DATA")
    else:
        lform=Login()
        return render(request,'login.html',{'lform':lform})