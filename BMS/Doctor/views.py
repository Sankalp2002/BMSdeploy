from django.shortcuts import render
from Doctor.forms import docregisterform
from Blood.views import home
from . import forms
#from django.http import HttpResponse
# from Doctor.forms import docregisterform

# Create your views here.
def doclogin(request):
    form=forms.docloginform()
    return render(request,'Doctor/doctorlogin.html',{'form':form})
 
def docregister(request):
    registered=False
    form=docregisterform()
    if request.method=='POST':
        form=docregisterform(data=request.POST)
        if form.is_valid():
            doc=form.save()
            doc.set_password(doc.password)
            doc.save()
            registered=True
            return home(request)
        else:
            print(docregisterform.errors)
    else:
        form=docregisterform()
    return render(request,'Doctor/registration.html',{'form':form,'registered':registered})

