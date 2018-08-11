from django.contrib import admin
from django.urls import path,include
from BasicApp import  views


app_name='BasicApp'
urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.user_login,name='login'),
]
