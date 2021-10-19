from django.urls import path,include

from . import views

urlpatterns=[
    path("",views.sullbey,name="sullbey"),
    path("<int:ido>/",views.specific,name="specific")
]