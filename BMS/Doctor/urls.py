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
    path('Panel/Patients/<int:pid>',views.delpatview,name='delpatview'),
    path('Panel/Donors/D/<int:pid>',views.deldonview,name='deldonview'),
    path('Panel/Requests',views.docpanelrlist,name='docpanelrlist'),
    path('Panel/Donors',views.docpaneldlist,name='docpaneldlist'),
    path('Panel/Requests/<int:rid>',views.cancelreq,name='cancelreq'),
    path('Panel/Donors/edit/<int:did>',views.editdonview,name='editdonview'),
    path('Panel/Donors/save/<int:did>',views.editdonsave,name='editdonsave'),
    path('Panel/Patients/edit/<int:did>',views.editpatview,name='editpatview'),
    path('Panel/Patients/save/<int:did>',views.editpatsave,name='editpatsave'),
    path('Panel/Donors/cancel/',views.editdoncancel,name='editdoncancel'),
    path('Panel/Patients/cancel/',views.editpatcancel,name='editpatcancel'),
]