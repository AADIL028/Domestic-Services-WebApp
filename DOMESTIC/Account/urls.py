from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.view_login,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('profile',views.profile),
    path('bookings',views.bookings),
    path('sign_up',views.sign_up,name="sign_up"),
    path('signup-emp',views.signupemp,name="signup-emp"),
    path('cart',views.cart,name="cart"),
    path('bookingform',views.bookingform,name="bookingform"),
    path('handlereq',views.handlereq,name="HandleReq"),
    path('makebooking',views.makeBooking,name="MakeBooking"),
    path('emp',views.emp,name="emp"), 
    path('emp_profile',views.emp_profile,name="Emp-Profile"), 
    path('cancelbooking',views.cancelBooking,name="CancelBooking"),
    path('completebooking',views.complete_booking,name="CompleteBooking"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
]