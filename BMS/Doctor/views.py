from django.shortcuts import render
from Doctor.forms import docregisterform
from Blood.views import home
#from django.http import HttpResponse
# from Doctor.forms import docregisterform

# Create your views here.
def doclogin(request):
    test1={'test1':"Hello Doctor"}
    return render(request,'Doctor/doctorlogin.html',context=test1)
 
def docregister(request):
    form=docregisterform()
    if request.method=='POST':
        form=docregisterform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('error')
            
    return render(request,'Doctor/registration.html',{'form':form})