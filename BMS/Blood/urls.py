from django.conf.urls import url
from Blood import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name='Blood'

urlpatterns=[
    path('',views.adminpanel,name='adminpanel'),
    path('Doctors/',views.adminpaneldoctor,name='adminpaneldoctor'),
    path('Donations/',views.adminpaneldonations,name='adminpaneldonations'),
    path('Donors/',views.adminpaneldonors,name='adminpaneldonors'),
    path('Patients/',views.adminpanelpatients,name='adminpanelpatients'),
    path('Requests/',views.adminpanelrequests,name='adminpanelrequests'),
    path('Requests/R/<int:rid>',views.rejreqview,name='rejreqview'),
    path('Requests/A/<int:qid>',views.appreqview,name='appreqview'),
    path('Donations/A/<int:did>',views.appdonview,name='appdonview'),
    path('Donations/R/<int:did>',views.rejdonview,name='rejdonview'),
    path('Patients/<int:pid>',views.delpatview,name='delpatview'),
    path('Doctors/D/<str:did>',views.deldocview,name='deldocview'),
    path('Donors/<int:did>',views.deldonview,name='deldonview'),
    path('Doctors/A/<int:did>',views.appdocview,name='appdocview'),
    path('Doctors/edit/<int:did>',views.editdocview,name='editdocview'),
    path('Doctors/save/<int:did>',views.editdocsave,name='editdocsave'),
    path('Doctors/cancel/',views.editdoccancel,name='editdoccancel'),
]