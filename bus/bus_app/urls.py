from django.urls import path
from .views import UserLoginView,UserRegisterView,BookingView,UserBookingView,BusDetailView, BusCreateView

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name="register"),
    path('login/',UserLoginView.as_view(),name='login'),
    path('bus/',BusCreateView.as_view(),name='bus'),
    path('user-booking/',UserBookingView.as_view(),name='user-booking'),
    path('bookings/',BookingView.as_view(),name="bookings"),

]