"""
URL configuration for gs7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from fees import views as fe
from course import views as co

coursepatterns = [
    path('coursedj/',co.learn_django),
    path('coursepy/',co.learn_python),
]

feespatterns = [
    path('feesdj',fe.fees_django),
    path('feespy',fe.fees_python),
]

urlpatterns = [

    path('admin/', admin.site.urls),
    path('cor/',include(coursepatterns)),
    path('fe/',include(feespatterns))
    
]
