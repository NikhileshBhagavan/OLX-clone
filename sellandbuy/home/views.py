from django.shortcuts import render,redirect
from sell.models import PRODUCT
from django.contrib import messages
from django.db import models
from django.http import *
# Create your views here.
def sullbey(request):
    if request.method=="GET":
        obj=PRODUCT.objects.all()
        ob=["hi","hello","bye"]

        return render(request,"sellbuy.html",{'obj':obj,'hel':ob})
    if request.method=="POST":
        a=request.POST['product']
        b=request.POST['state'].lower().replace(" ",'')
        c=request.POST['city'].lower().replace(" ",'')
        obj=PRODUCT.objects.filter(category=a,state=b,city=c)

        
        if obj.exists():
            return render(request,"sellbuy.html",{'obj':obj})
        else:
            messages.info(request,"No such product with that specifications present")
            return redirect("/login/home/")
def specific(request,ido):
    obj=PRODUCT.objects.get(id=ido)
    obj.hello()
    return render(request,"specificproduct.html",{'obj':obj})