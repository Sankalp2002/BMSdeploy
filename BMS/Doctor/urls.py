from django.conf.urls import url
from Doctor import views
from django.urls import path

app_name='Doctor'

urlpatterns=[
    path('Login/',views.doclogin,name='doclogin'),
    path('Register/',views.docregister,name='docregister'),
    #path('panel/',views.docpanel,name='docpanel'),
]