from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    category=models.CharField(max_length=50)
    title=models.TextField()
    description=models.TextField()
    price=models.IntegerField()
    mainimg=models.FileField(upload_to="pictures/")
    img1=models.FileField(upload_to="pictures/",default=None)
    img2=models.FileField(upload_to="pictures/")
    img3=models.FileField(upload_to="pictures/")
    
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    contactnumber=models.CharField(max_length=100)
    sellername=models.CharField(max_length=150)
    def hello(self):
        print("hellosdnvjkdnvnkjndjkvn")