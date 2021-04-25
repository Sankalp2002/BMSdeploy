# from django.shortcuts import render
# from Donor.forms import NewDonorForm
# from Doctor import views

# # Create your views here.
# def newdonor(request):
#     form=NewDonorForm()
#     if request.method=="POST":
#         form= NewDonorForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return docpanel(request)
#         else:
#             print('Error')
#     return render(request,'Doctor/doctorpaneldonor.html',{'form':form})