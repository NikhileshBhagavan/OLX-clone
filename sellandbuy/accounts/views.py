from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random
import math
# Create your views here.

def homepage(request):
    if request.method=="GET":
        return render(request,"signup.html")
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]
        if password1==password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                    user.save()
                    subject = 'Donot reply'
                    name=user.first_name
                    message = 'Hi'+name+"THANK YOU FOR REGISTERING IN S&B"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email]
                    send_mail( subject, message, email_from, recipient_list )
                else:
                    messages.info(request,"email taken,please register again")
                    return redirect('/')

            else:
                messages.info(request,"username Taken,please register again")
                return redirect("/")

        
        else:
            messages.info(request,"Passwords Not matching,Please Register again")
            return redirect("/")
        return redirect("/login/")

def login(request):
    if request.method=="POST":
        username=request.POST['your_name']
        password=request.POST['your_pass']
        
        objo=auth.authenticate(username=username,password=password)
        print(request.user.is_authenticated)
        # returns user object if present
        if objo is not None:
            auth.login(request,objo)
            return redirect("/login/home/")
        else:
            messages.info(request,"USER NOT FOUND ,PLEASE CHECK YOUR USERNAME AND PASSWORD AGAIN")
            return redirect("/login/")

    if request.method=="GET":
        return render(request,"signin.html")

def checkout(request):
    auth.logout(request)
    
    return redirect("/")

obj=None
otp=None
def GENERATEOTP():
    s="0123456789"
    b=""
    for i in range(8):
        b=b+s[int(random.random()*10)]
    return b
def forgotpassword(request):
    if request.method=='GET':
        return render(request,"forgotpassword.html")
    if request.method=='POST':
        username=request.POST["username"]
        email=request.POST["email"]
        try:
            globals()['obj']=User.objects.get(username=username,email=email)
            subject = 'Donot reply'
            globals()["otp"]=GENERATEOTP()
            name=globals()['obj'].first_name
            message = 'Hi'+name+"YOUR OTP TO SET PASSWORD IS "+otp
            recipient_list = [globals()['obj'].email]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message, email_from, recipient_list )
            return redirect("/login/forgpas/confirm")
        except:
            messages.info(request,"USERNAME AND EMAIL ARE NOT MATCHING OR NOT FOUND")
            return redirect("/login/forgpas")

def lemmecheck(request):
    if request.method=="GET":
        return render(request,"confirm.html")
    if request.method=="POST":
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if globals()['otp']==request.POST["OTP"]:
                globals()['obj'].set_password(password1)
                globals()['obj'].save()
                return redirect("/login/")
            else:
                messages.info(request,"OTP's not matching,check again")
                return redirect("/login/forgpas/confirm")
        else:
            messages.info(request,"PASSWORD's not matching")
            return redirect("login/forgpas/confirm")
