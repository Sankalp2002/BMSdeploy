from django.conf.urls import url
from Doctor import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name='Doctor'

urlpatterns=[
    path('Login/',views.doclogin,name='doclogin'),
    path('Register/',views.docregister,name='docregister'),
    path('Panel/',views.docpanel,name='docpanel'),
    path('Request/new/',views.docpanelrequest,name='docpanelrequest'),
    path('Donation/new/',views.docpanelnewdon,name='docpanelnewdon'),
    path('Donor/new/',views.docpaneldonor,name='docpaneldonor'),
    path('Patient/new/',views.docpanelpatient,name='docpanelpatient'),
    path('Patient/list/',views.docpanelplist,name='docpanelplist'),
    path('Patient/delete/<str:pid>',views.delpatview,name='delpatview'),
    path('Donors/delete/<str:pid>',views.deldonview,name='deldonview'),
    path('Request/list/',views.docpanelrlist,name='docpanelrlist'),
    path('Donor/list/',views.docpaneldlist,name='docpaneldlist'),
    path('Request/cancel/<int:rid>',views.cancelreq,name='cancelreq'),
    path('Donor/edit/<str:did>',views.editdonview,name='editdonview'),
    path('Donor/save/<str:did>',views.editdonsave,name='editdonsave'),
    path('Patient/edit/<str:did>',views.editpatview,name='editpatview'),
    path('Patient/save/<str:did>',views.editpatsave,name='editpatsave'),
    path('Donor/edit/cancel/',views.editdoncancel,name='editdoncancel'),
    path('Patient/edit/cancel/',views.editpatcancel,name='editpatcancel'),
]