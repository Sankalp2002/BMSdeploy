from django.conf.urls import url
from Blood import views
from django.urls import path

app_name='Blood'

urlpatterns=[
    #path('Home/',views.home,name='home'),
    path('Login/',views.adminlogin,name='adminlogin'),
    path('Panel/',views.adminpanel,name='adminpanel'),
]