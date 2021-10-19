from django.shortcuts import render,redirect
from .models import PRODUCT
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def sellproduct(request):
    if request.method=="GET":
        return render(request,"product.html")
    if request.method=="POST":
        obj=PRODUCT()
        
        obj.category=request.POST['product']
        obj.title=request.POST['title']
        obj.description=request.POST['description']
        
        obj.price=int(request.POST['price'])
        obj.mainimg=request.FILES['Mainimage']
        obj.img1=request.FILES['image1']
        obj.img2=request.FILES['image2']
        obj.img3=request.FILES['image3']
        obj.state=request.POST['state'].lower().replace(" ",'')
        obj.city=request.POST['city'].lower().replace(" ",'')
        obj.contactnumber=request.POST['contnum']
        obj.sellername=request.user.username
        obj.save()
        messages.info(request,"Ur product has uploaded into my database")
        return redirect("/login/home/")