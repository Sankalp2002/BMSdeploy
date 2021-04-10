"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Doctor import views as dviews
# from Patient import views as pviews
# from Donor import views as doviews
from Blood import views as bviews

urlpatterns = [
    path('',bviews.home,name='home'),
    path('admin/', admin.site.urls),
    path('Doctor/',include('Doctor.urls')),
    path('Adminlogin/',bviews.adminlogin,name='adminlogin'),
    # path('Patient/',include('Patient.urls')),
    # path('Donor/',include('Donor.urls'))
]
