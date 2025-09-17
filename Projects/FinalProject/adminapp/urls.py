from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
   path('',views.admin_login),
   path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
   path('userdata/',views.userdata,name='userdata'),
   path('notesdata/',views.notesdata,name='notesdata'),
   path('approve_notes/<int:id>',views.approve_notes,name='approve_notes'),
   path('reject_notes/<int:id>',views.reject_notes,name='reject_notes'),
]
