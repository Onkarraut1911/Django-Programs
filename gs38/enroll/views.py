    
from django.shortcuts import render
from .forms import student_login
from django.http import HttpResponseRedirect

def thankyou(request):
    return render(request,'enroll/success.html')

def student_registration(request):
    if request.method == 'POST':
        fm = student_login(request.POST)
        if fm.is_valid():
            print('form validated')
            name = fm.cleaned_data['first_name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('name',name)
            print('email',email)
            print('password',password)
            return HttpResponseRedirect('/regi/success/')
            # return render(request,'enroll/success.html',{'nm':name})

    else:
        fm = student_login()
        print("ye get se request aya he")

    return render(request,'enroll/Student_registration.html',{"form":fm})



# from django.shortcuts import render
# from .forms import student_login # Replace with the actual import for your form

# def student_registration(request):
#     if request.method == 'POST':
#         fm = student_login(request.POST)
#         if fm.is_valid():
#             print('form validated')
#             name = fm.cleaned_data['first_name']
#             email = fm.cleaned_data['email']
#             password = fm.cleaned_data['password']
#             print('name',name)
#             print('email',email)
#             print('password',password)
#             return render(request,'enroll/success.html',{'nm':name})
#     else:
#         fm = student_login()
    
#     return render(request, 'enroll/Student_registration.html', {'form': fm})
