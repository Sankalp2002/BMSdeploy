from django.conf.urls import url
from Doctor import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name='Doctor'

urlpatterns=[
    path('Login/',views.doclogin,name='doclogin'),
    #path('Login/', LoginView.as_view(template_name='Doctor/doctorlogin.html'), name='doclogin'),
    path('Register/',views.docregister,name='docregister'),
    path('Panel/',views.docpanel,name='docpanel'),
    path('Panel/NewRequest',views.docpanelrequest,name='docpanelrequest'),
    path('Panel/NewDonation',views.docpanelnewdon,name='docpanelnewdon'),
    path('Panel/Donor',views.docpaneldonor,name='docpaneldonor'),
    path('Panel/NewPatient',views.docpanelpatient,name='docpanelpatient'),
    path('Panel/Patients',views.docpanelplist,name='docpanelplist'),
    path('Panel/Requests',views.docpanelrlist,name='docpanelrlist'),
]