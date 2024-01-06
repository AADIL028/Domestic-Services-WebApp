from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('cleanning',views.cleanning,name="cleanning"),
    path('carpenter',views.carpenter,name="carpenter"),
    path('electrics',views.electrics,name="electrics"),
    path('plumbing',views.plumbing,name="plumbing"),
    path('add_to_cart/<str:cat>/<int:sno>',views.add_to_cart,name="add_to_cart"),
    path('remove_item',views.remove_item,name="remove_item"),
]