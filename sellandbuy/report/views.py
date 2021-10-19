from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def adcheck(request):
    if request.method=="GET":
        return render(request,"report.html")
    if request.method=="POST":
        mes=request.POST["description"]
        subject = 'Report from S&B User'+request.user.username
        message = mes
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kancharla_nb@cs.iitr.ac.in']
        send_mail( subject, message, email_from, recipient_list )
        messages.info(request,"Your report submitted successfully")
        return redirect("/login/home/")