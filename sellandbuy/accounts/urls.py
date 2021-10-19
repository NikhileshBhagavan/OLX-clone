from django.urls import path,include 

from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login/',views.login,name="login"),
    path('logout/',views.checkout,name="checkout"),
    path('login/forgpas',views.forgotpassword,name="forgotpassword"),
    path('login/forgpas/confirm',views.lemmecheck,name="lemmecheck")
]