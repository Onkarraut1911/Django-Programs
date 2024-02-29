from django.shortcuts import render
from .forms import Student_Registration,Teacher_Registration
# Create your views here.
def student_form(request):
  if request.method == 'POST':
    fm = Student_Registration(request.POST)
    if fm.is_valid():
      fm.save()
  else:
    fm = Student_Registration()
  return render(request,'enroll/student.html',{'form':fm})

def teacher_form(request):
  if request.method == 'POST':
    fm = Teacher_Registration(request.POST)
    if fm.is_valid():
      fm.save()

  else:
    fm = Teacher_Registration()
  return render(request,'enroll/teacher.html',{'form':fm})
