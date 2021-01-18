from django.urls import path
from .views import HallListView,BookingListView,BookingView,confirm_booking
urlpatterns = [
    
    path('',HallListView.as_view(),name='HallListView'),
    path('bookings',BookingListView.as_view(),name='BookingListView'),
    path('book',BookingView.as_view(),name='BookingView'),
    path('confirm_book/<int:id>',confirm_booking,name='confirm_booking'),
    ]
