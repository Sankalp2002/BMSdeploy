from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from Doctor import views as dviews
from Blood import views as bviews


urlpatterns = [
    path('',bviews.home,name='home'),
    path('admin/', admin.site.urls),
    path('Doctor/',include('Doctor.urls')),
    path('Admin/',include('Blood.urls')),
    path('logout/',dviews.doclogout,name='doclogout'),
    path('adminlogout/',bviews.adminlogout,name='adminlogout'),
    # path('Patient/',include('Patient.urls')),
    # path('Donor/',include('Donor.urls'))
    path('<path:e>/',bviews.errorview,name='errorview'),
]
