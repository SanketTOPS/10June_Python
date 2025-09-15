from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
   path('',views.admin_login),
   path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
   path('userdata/',views.userdata,name='userdata'),
]
