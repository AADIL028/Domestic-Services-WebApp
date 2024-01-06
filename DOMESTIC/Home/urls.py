from django.contrib import admin
from django.urls import path,include
from . import views
from Services import views as sv
from Account import views as av
from django.contrib.auth import views as auth_views


urlpatterns = (
    path('', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('bookingform/', av.bookingform, name="bookingform"),
    path('cleanning/',sv.cleanning,name="cleanning"),
    path('plumbing/',sv.plumbing,name="plumbing"),
    path('electrics/',sv.electrics,name="electrics"),
    path('carpenter/',sv.carpenter,name="carpenter"),
    path('login/',av.view_login,name="login"),
    path('logout/',av.logout_view,name="logout"),
    path('profile/',av.profile),
    path('bookings/',av.bookings),
    path('cart/', av.cart, name="cart"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('account/sign_up',av.sign_up,name="sign_up"),
    path('account/signup-emp',av.signupemp,name="signup-emp"),
    path('add_to_cart',sv.add_to_cart,name="add_to_cart"),
    path('makebooking',av.makeBooking,name="MakeBooking"),
    path('cancelbooking',av.cancelBooking,name="CancelBooking"),
    path('completebooking',av.complete_booking,name="CompleteBooking"),
    path('emp',av.emp,name="Employee"),
    path('emp_profile',av.emp_profile,name="Emp-Profile"),
)