from django.urls import path,include

from . import views


urlpatterns=[
    path('',views.adcheck,name="adcheck")
]