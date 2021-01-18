from django.urls import path
from .views import listHalls,BookingHalls,createBooking

urlpatterns = [
    
    path('halls',listHalls,name='listHalls'),
    path('booking',BookingHalls,name='BookingHalls'),
    path('createBooking',createBooking,name='createBooking'),
]
