from django.conf.urls import url
from Doctor import views
from django.urls import path

urlpatterns=[
    path('login/',views.doclogin,name='doclogin'),
    path('register/',views.docregister,name='docregister'),
]