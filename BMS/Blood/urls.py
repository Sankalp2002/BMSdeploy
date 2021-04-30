from django.conf.urls import url
from Blood import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name='Blood'

urlpatterns=[
    path('',views.adminpanel,name='adminpanel'),
    path('Doctor/list/',views.adminpaneldoctor,name='adminpaneldoctor'),
    path('Donation/list/',views.adminpaneldonations,name='adminpaneldonations'),
    path('Donor/list/',views.adminpaneldonors,name='adminpaneldonors'),
    path('Patient/list/',views.adminpanelpatients,name='adminpanelpatients'),
    path('Request/list/',views.adminpanelrequests,name='adminpanelrequests'),
    path('Request/reject/<int:rid>',views.rejreqview,name='rejreqview'),
    path('Request/approve/<int:qid>',views.appreqview,name='appreqview'),
    path('Donation/approve/<int:did>',views.appdonview,name='appdonview'),
    path('Donation/reject/<int:did>',views.rejdonview,name='rejdonview'),
    path('Patient/delete/<int:pid>',views.delpatview,name='delpatview'),
    path('Doctor/delete/<str:did>',views.deldocview,name='deldocview'),
    path('Donor/delete/<int:did>',views.deldonview,name='deldonview'),
    path('Doctor/approve/<int:did>',views.appdocview,name='appdocview'),
    path('Doctor/edit/<int:did>',views.editdocview,name='editdocview'),
    path('Doctor/edit/save/<int:did>',views.editdocsave,name='editdocsave'),
    path('Doctor/cancel/',views.editdoccancel,name='editdoccancel'),
    path('Hospital/add/',views.newhospital,name='newhospital'),
    path('Hospital/edit/<int:id>',views.edithospital,name='edithospital'),
    path('Hospital/save/edit/<int:id>',views.edithossave,name='edithossave'),
    path('Hospital/delete/<int:id>',views.delhospital,name='delhospital'),
    path('Hospital/list/',views.listhospital,name='listhospital'),
]