from django.conf.urls import url
from Blood import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name='Blood'

urlpatterns=[
    #path('Home/',views.home,name='home'),
    path('Login/',views.adminlogin,name='adminlogin'),
    #path('Login/', LoginView.as_view(template_name='Blood/adminlogin.html'), name='adminlogin'),
    path('Panel/',views.adminpanel,name='adminpanel'),
    path('Panel/Doctor/',views.adminpaneldoctor,name='adminpaneldoctor'),
    path('Panel/Donations/',views.adminpaneldonations,name='adminpaneldonations'),
    path('Panel/Donors/',views.adminpaneldonors,name='adminpaneldonors'),
    path('Panel/Patients/',views.adminpanelpatients,name='adminpanelpatients'),
    path('Panel/Requests/',views.adminpanelrequests,name='adminpanelrequests'),
]