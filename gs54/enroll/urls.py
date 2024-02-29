# from django.urls import path , register_converter
# from . import views , converters
# register_converter(converters.FourDigitYearConverter, 'yyyy')
# urlpatterns = [
#     path('sesstion/<yyyy:year/',views.show_details, name='details'),
# ]

from django.urls import path , register_converter
from . import views , converters

# Register the four-digit year converter.
register_converter(converters.FourDigitYearConverter, 'yyyy')

# Define a URL pattern that uses the four-digit year converter.
urlpatterns = [
    path('sesstion/<yyyy:year>/', views.show_details, name='details'),
]
  