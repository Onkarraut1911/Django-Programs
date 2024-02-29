from django.contrib import admin
from enroll.models import student
# Register your models here.
@admin.register(student)
class studnetadmin(admin.ModelAdmin):
   list_display = ('stuid','stuname' , 'stuemail' , 'stupass')
# admin.site.register(student,studnetadmin)