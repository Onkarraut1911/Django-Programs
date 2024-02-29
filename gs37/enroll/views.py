from django.shortcuts import render
from .forms import STUDENT_REGISTRATION
# Create your views here.
def Student_Registration(request):
    if request.method == 'POST':
        STU_DATA = STUDENT_REGISTRATION(request.POST)
        if STU_DATA.is_valid():
            # print(STU_DATA)
            # print("ye post request se aya hei")
            # print('clean DATA : ',STU_DATA.cleaned_data)
            print('form validated')
            # print('First Name : ',STU_DATA.cleaned_data['first_name'])
            # print('Email : ',STU_DATA.cleaned_data['email'])
            name = STU_DATA.cleaned_data['first_name']
            email = STU_DATA.cleaned_data['email']
            print('name',name)
            print('email',email)
            # STU_DATA = STUDENT_REGISTRATION()
    else:
        STU_DATA = STUDENT_REGISTRATION()
        print("ye get request se aya hei")
    # STU_DATA = STUDENT_REGISTRATION()
    return render(request,"enroll\student_registration.html",{"form":STU_DATA})