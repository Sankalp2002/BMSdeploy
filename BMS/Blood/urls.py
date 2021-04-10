from django.conf.urls import url
from Blood import views
from django.urls import path

urlpatterns=[
    path('home/',views.home,name='home'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
]