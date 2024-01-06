from django.contrib import admin
from .models import Cleaning,Electics,Plumbing,Carpenter,Review
# Register your models here.

admin.site.register(Cleaning)
admin.site.register(Electics)
admin.site.register(Plumbing)
admin.site.register(Carpenter)
admin.site.register(Review)
