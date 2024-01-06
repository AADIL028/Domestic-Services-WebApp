from django.contrib import admin
from .models import Empdetails,Signup,Bookings
# Register your models here.
# admin.site.register(UserDetails)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username','fname','lname','phone','email','address','work')
    list_editable = ('fname','lname','phone','email','address','work')
    exclude = ('password',)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','fname','lname','phone','email','address')
    list_editable = ('fname','lname','phone','email','address')
    exclude = ('password',)

admin.site.register(Empdetails,EmployeeAdmin)
admin.site.register(Signup,UserAdmin)
admin.site.register(Bookings)